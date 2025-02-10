"""
1 Vilka ekvivalensklasser har uttrycken?
1a. x > 100
    > * Allt som är mindre än 100 (false) dvs 99, 98, 97, ...
      * 100 (false)  <--- INTE en ekvivalensklass
      * Allt som är större än 100 (true) dvs 101, 102, ...

    Rättning:
    Endast 2 ekvivalensklasser
     * {100,99,98,97, ....}
     * {101,102,103, ...}

1b. y == 42
    > * 42 (true)
      * Allt tal som inte är 42 (false) dvs 41, 40, 39,... och 43, 44, ... 

    {42} och {alla andra tal än 42}
    
1c. len(text) >= 5
    > * Allt som är mindre än 5 (false) dvs 4, 3, ...
      * Allt som är 5 eller högre (true) dvs 5, 6, ...

    Rättning 2: {5, 6,...} och {0, 1, 2, 3, 4} inga negativa tal eftersom
    strängar inte kan ha negativt antal tecken.

1d. z == True
    > * True (true)
      * False (false)
      
1e. 8 < v < 16
    > * Allt som är högre än 8 men mindre än 16 (true), 9, 10, 11, 12, 13, 14 och 15
      * Allt som är mindre än 8 (false) dvs 7, 6, ..
      * Allt som är ströre än 16 (false) dvs 17, 18, 19, ...

    Rättning: gränserna måste också ingå någonstans dvs 8 och 16
     * {8, 7, 6, ...}
     * {16, 17, 18, ...}
     * {9, 10, 11, 12, 13, 14, 15}
    
1f. w == 32 or w == 64 or w == 128
    > 2 ekvivalensklass
       * När w är 32, 64 eller 128 (true) -> {32, 64, 128}
       * Övrigt (false)                   -> { alla andra tal}
      
1g. if x < 5: … elif x < 10: … elif x < 15: … else
    > 4 ekvivalensklass
       * mindre än 5 - > {4, 3, 2, ...}
       * mindre än 10 men mer än 5 -> {9, 8, 7, 6, 5} kan inte gå längre ner
         eftersom de redan ingår i ena annan ekvivalensklass 
       * mindre än 15 men mer än 10 -> {14, 13, 12, 11, 10}
         samma sakm här inte lägre pga att de ingår i en annan ekvivalensklass
       * mer än 15 -> {15, 16, 17, ...}
"""