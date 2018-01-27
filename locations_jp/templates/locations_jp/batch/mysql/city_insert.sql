INSERT {{ city_master }}
(
  jiscode,
  name,
  kana,
  prefecture_id
)
SELECT
  SRC.jiscode,
  SRC.name,
  SRC.kana,
  SRC.prefecture_id
FROM {{ city_import }} AS SRC
LEFT JOIN {{ city_master }} as DST
ON
  DST.jiscode = SRC.jiscode AND
  DST.name = SRC.name AND
  DST.kana = SRC.kana
WHERE
  DST.jiscode is NULL;
