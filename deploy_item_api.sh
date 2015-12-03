#!/bin/sh
kill -9 `cat item_api/pid`
#rm item_api/pid
if [ "$1" = "recreate_db" ]; then
    psql -Uitem_api -dpostgres < db/data/recreate_db.sql
elif [ "$1" = "reload" ]; then
    echo "reload"
else
    rz
    mv item_api.zip item_api/item_api.zip
    cd item_api
    unzip -o item_api.zip
    rm item_api.zip
    cd ..
fi

#cd item_api
nohup python -u app.py > out.log 2>&1 &