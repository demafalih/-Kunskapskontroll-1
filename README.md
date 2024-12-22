Pythonskript för flödet och tester. Pga att jag har en mac så har jag inte kunnat skapa en "vanlig" schemaläggning, men en skärmdump finns där ändå.



Python-Projekt som bearbetar ett dataset om bilar för att:
- Läsa in data från en CSV-fil som sköts av funktionen load_data(file_path)
- Filtrera bilar med hästkrafter över 190 som sköts av funktionen filter_horsepower(df)
- Spara bilarna till SQLite-databas som sköts av funktionen save_to_database(df, db_path)
- Jämför genomsnittlig hästkraft mellan bilar från USA och Europa som sköts av funktionen compare_origin_hp(df)

Krav
- Python 3
- SQLite för att lagra data
- Pandas för att hantera och bearbeta data (t.ex filtrering, gruppering, beräkningar)

När skriptet körs, kan man få resultat som:
- "Cars of origin USA have higher average horsepower."
- "Cars of origin European have higher average horsepower."
- "Cars of origin 'USA' and 'European' have the same average horsepower."
