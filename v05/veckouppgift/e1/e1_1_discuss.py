"""
1 Vilka ekvivalensklasser har uttrycken?
1a. x > 100
    > * Allt som är mindre än 100 (false) dvs 99, 98, 97, ...
      * 100 (false)
      * Allt som är större än 100 (true) dvs 101, 102, ...

1b. y == 42
    > * 42 (true)
      * Allt som inte är 42 (false) dvs 41, 40, 39,... och 43, 44, ... 

1c. len(text) >= 5
    > * Allt som är mindre än 5 (false) dvs 4, 3, ...
      * Allt som är 5 eller högre (true) dvs 5, 6, ...

1d. z == True
    > * True (true)
      * False (false)
      
1e. 8 < v < 16
    > * Allt som är högre än 8 men mindre än 16 (true), 9, 10, 11, 12, 13, 14 och 15
      * Allt som är mindre än 8 (false) dvs 7, 6, ..
      * Allt som är ströre än 16 (false) dvs 17, 18, 19, ...

1f. w == 32 or w == 64 or w == 128
    > * När w är 32, 64 eller 128 (true)
      * Övrigt (fasle)


1g. if x < 5: … elif x < 10: … elif x < 15: … else
    > * mindre än 5
      * mindre än 10 menm mer än 5
      * mindre än 15 men mer än 10
      * mer än 15
"""