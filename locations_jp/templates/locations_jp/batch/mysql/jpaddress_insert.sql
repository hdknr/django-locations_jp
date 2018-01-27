INSERT {{ jpaddress_master }}
(
  jiscode,
  zipcode5,
  zipcode,
  pref_kana,
  city_kana,
  town_kana,
  pref_name,
  city_name,
  town_name,
  is_split,
  is_small,
  is_towncode,
  is_multi,
  is_changed,
  reason,
  md5
)
SELECT
  SRC.jiscode,
  SRC.zipcode5,
  SRC.zipcode,
  SRC.pref_kana,
  SRC.city_kana,
  SRC.town_kana,
  SRC.pref_name,
  SRC.city_name,
  SRC.town_name,
  SRC.is_split,
  SRC.is_small,
  SRC.is_towncode,
  SRC.is_multi,
  SRC.is_changed,
  SRC.reason,
  SRC.md5
FROM {{ jpaddress_import }} AS SRC
LEFT JOIN {{ jpaddress_master }} as DST
ON
  DST.md5 = SRC.md5
WHERE
  DST.md5 is NULL;

UPDATE {{ jpaddress_master }} as DST INNER JOIN
{{ city_master }} as SRC ON
DST.jiscode = SRC.jiscode
SET
DST.city_id = SRC.id
WHERE
DST.city_id is NULL;
