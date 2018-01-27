--
UPDATE {{ city_master }} as DST INNER JOIN
{{ city_import }} as SRC ON
DST.jiscode = SRC.jiscode AND
DST.name = SRC.name AND
DST.kana = SRC.kana
SET
DST.prefecture_id = SRC.prefecture_id;
