#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the classes Dbread and Dbtracks. This classes let us
handle more easily sqlite databases and Dbtracks have specials attributes
for the 'track_metadata.db' database from MSongDB.
"""
import sqlite3 as lite


class Dbread:
    """
    little helper for the management of sqlite databases
    """
    def __init__(self, dbfile, memory=1000):
        self.file = dbfile
        self.open()
        self.memory = memory
        self.historic = []

    def open(self):
        self.sqldb = lite.connect(self.file, isolation_level=None)
        self.cur = self.sqldb.cursor()

    def close(self):
        self.cur.close()
        self.sqldb.close()

    @property
    def tables(self):
        """
        get all table names in the database
        """
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self.cur.fetchone()

    @property
    def nbtables(self):
        return len(self.tables)

    def columns(self, table):
        """
        get the column names and types from the inputed table
        """
        self.cur.execute("PRAGMA table_info('" + table + "')")
        return [x[:3] for x in self.cur.fetchall()]

    def request(self, query, mem=True):
        """
        execute a query and return the result
        """
        self.cur.execute(query)
        if mem:
            self.__update_historic(query)
        return self.cur.fetchall()

    def __update_historic(self, up):
        """
        hidden method updating the historic with the size constraint
        """
        if len(self.historic) == self.memory:
            self.historic = self.historic[1:]
        self.historic.append(up)

    def commit(self):
        self.sqldb.commit()


class Dbtracks(Dbread):
    """
    specific for the management of the songs table from the database
    track_metadata.db
    """
    @property
    def artists(self):
        """
        All the artist names
        """
        return self.request("SELECT DISTINCT artist_id, artist_name " +
                            "FROM songs", mem=False)

    @property
    def tracks(self):
        """
        all the tracks
        """
        return self.request("SELECT track_id, title, artist_name FROM songs",
                            mem=False)

    @property
    def nbtracks(self):
        return len(self.tracks)

    @property
    def nbartists(self):
        return len(self.artists)


# Example
if __name__ == "__main__":
    DB_FOLDER = "db/"
    DBFILE = DB_FOLDER + 'track_metadata.db'
    sqldb = Dbtracks(DBFILE)
    print("#-------------------------------------------------------#")
    print("#          database : " + str(sqldb.file))
    print("#            tables : " + str(sqldb.tables))
    print("# nombre d'artistes : " + str(sqldb.nbartists))
    print("# nombre de pistes  : " + str(sqldb.nbtracks) + "\n")
    print("---- les colonnes de la table songs ----")
    for i in range(len(sqldb.columns("songs"))):
        print(sqldb.columns("songs")[i])
    print("\n l'historique (vide) : " + str(sqldb.historic))
    print(" taille max de l'historique" + str(sqldb.memory))
    print("#-------------------------------------------------------#")
    sqldb.close()
