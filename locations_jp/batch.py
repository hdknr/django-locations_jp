from tempfile import TemporaryFile
from hashlib import md5
import csv
import unicodedata
from . import utils, models, defs


def mysql_jpaddress_import(file, out=None, dry=False):
    names = [f.name for f in defs.JpAddress._meta.fields]
    table = models.JpAddressImport._meta.db_table

    out = out or TemporaryFile(mode='w+t')
    out.write("TRUNCATE TABLE {};\n".format(table))
    out.write("INSERT INTO {}\n".format(table))
    out.write("({})\n".format(",".join(names)))

    SEP = ' VALUES '
    for row in csv.reader(file):
        row.append("'{}'".format(
            md5("".join(row).encode('utf8')).hexdigest()))
        for i in range(len(row)):
            if i in [3, 4, 5]:
                row[i] = "'{}'".format(
                    unicodedata.normalize('NFKC', row[i]))
            elif i <= 8:
                row[i] = "'{}'".format(row[i])
        out.write("{} ({})\n".format(SEP, ",".join(row)))
        SEP = ", "
    out.write(";\n");

    if not dry:
        out.seek(0)
        sql = out.read()
        utils.call_sql(sql)
        
    out.close()


def mysql_city_import(dry=False):
    sql = utils.render_by(
        'locations_jp/batch/mysql/city_import.sql',
        city_import=models.CityImport._meta.db_table,
        jpaddress_import=models.JpAddressImport._meta.db_table,
        prefecture=models.Prefecture._meta.db_table,
    )
    if dry:
        return sql
    utils.call_sql(sql)


def mysql_city_update(dry=False):
    sql = utils.render_by(
        'locations_jp/batch/mysql/city_update.sql',
        city_import=models.CityImport._meta.db_table,
        city_master=models.City._meta.db_table,
    )
    if dry:
        return sql
    utils.call_sql(sql)


def mysql_city_insert(dry=False):
    sql = utils.render_by(
        'locations_jp/batch/mysql/city_insert.sql',
        city_import=models.CityImport._meta.db_table,
        city_master=models.City._meta.db_table,
    )
    if dry:
        return sql
    utils.call_sql(sql)



def mysql_jpaddress_insert(dry=False):
    sql = utils.render_by(
        'locations_jp/batch/mysql/jpaddress_insert.sql',
        city_master=models.City._meta.db_table,
        jpaddress_master=models.JpAddress._meta.db_table,
        jpaddress_import=models.JpAddressImport._meta.db_table,
    )
    if dry:
        return sql
    utils.call_sql(sql)
