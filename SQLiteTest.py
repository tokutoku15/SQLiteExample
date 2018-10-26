import sqlite3

def main():
    #example.dbがなければ作成、あればアクセス
    #第二引数で自動コミット
    con = sqlite3.connect('example.db',isolation_level=None)
    print(con)

    # カーソルオブジェクトを作成
    cursor = con.cursor()
    print(cursor)

    #テーブルの中身を削除
    cursor.execute('delete from data_set')
    
    #テーブルを作成
    #cursor.execute("CREATE TABLE data_set(id,name,date)")
    
    #テーブルにデータを追加する
    #脆弱性あり(SQLインジェクション)
    #cursor.execute("INSERT INTO data_set VALUES(1, 'tokutoku15', 19970715)")
    #安全なデータ追加
    p = "INSERT INTO data_set(id,name,date) VALUES(?,?,?)"
    cursor.execute(p,(1,'tokutoku15',19970715))
    #複数業データ
    data = [
            (1,"saito",19990810),
            (2,"tadokoro",19750810),
            (3,"yamada",19801010),
            (4,"sato",19450411),
            (5,"tanaka",20001121),
            ]
    #複数データの挿入
    cursor.executemany(p,data)

    #データベースに反映させる
    #con.commit()

    #データベースを取得
    cursor.execute('SELECT * FROM data_set')
    results = cursor.fetchall()
    print(results)

if __name__ == '__main__':
    main()
