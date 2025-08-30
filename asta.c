#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "giocatore.h"
#include "allenatore.h"

int main (int argc, char *argv[])
{
   
    int i;
    int j;
    int numPartecipanti=atoi(argv[2]);
    int azione = 0;
    int selezione;
    int contatoreRosa = 0;
   
    FILE *fPtr;
    
    
    ALLENATORE squadre [numPartecipanti];
    int contatoreInterno [numPartecipanti];
    char *giocatori_str = strdup(argv[4]); // duplica la stringa
char *token = strtok(giocatori_str, ","); // primo token

for (i = 0; i < numPartecipanti; i++) {
    if (token == NULL) {
        printf("Mancano nomi sufficienti!\n");
        fflush(stdout); 
        break;
    }
    strncpy(squadre[i].nomeAllenatore, token, sizeof(squadre[i].nomeAllenatore) - 1);
    squadre[i].nomeAllenatore[sizeof(squadre[i].nomeAllenatore)-1] = '\0';

    token = strtok(NULL, ","); 
    squadre[i].budget = atoi(argv[2]);
    squadre[i].numG = i + 1;
    contatoreInterno[i] = 0;

    
}

    free(giocatori_str);
    
    printf ("Recap delle squadre: \n");
    fflush(stdout); 
    
    for (i=0; i < numPartecipanti; i++)
    {
        printf ("%d. %s\n", squadre[i].numG, squadre[i].nomeAllenatore);
        fflush(stdout); 
    }
    
    printf ("\n");
    
    while (azione == 0)
    {
          printf ("Seleziona la squadra dal men�: \n");
          fflush(stdout); 
          
           for (i=0; i < numPartecipanti; i++)
            {
                printf ("%d. %s\n", squadre[i].numG, squadre[i].nomeAllenatore);
                fflush(stdout); 
            }
            
            scanf ("%d", &selezione);
            fflush (stdin);
            
            if (selezione < 1 || selezione > 8)
            {
                while (selezione < 1 || selezione > 8)
                {
                     printf ("Squadra non valida. Riprova\n");
                     fflush(stdout); 
                }
            }
            
            contatoreInterno [selezione] ++;
            
            printf ("Inserisci nome del giocatore: \n");
            fflush(stdout); 
            gets (squadre[selezione].nomiGiocatori[contatoreInterno [selezione-1]].nomeGiocatore);
            fflush (stdin);
            
            printf ("Inserisci il prezzo: \n");
            fflush(stdout); 
            scanf ("%d", &squadre[selezione].nomiGiocatori[contatoreInterno [selezione-1]].prezzo);
            fflush (stdin);
            
            if (squadre[selezione].budget < 500 && squadre[selezione].budget - squadre[selezione].nomiGiocatori[contatoreInterno [selezione-1]].prezzo < 0)
            {
                printf ("Credito insufficiente, riprova\n");
                fflush(stdout); 
                contatoreInterno [selezione] --;
            }
            
            else
            {
                system ("clear");
                printf ("Giocatore aggiunto correttamente\n\n");
                fflush(stdout); 
                contatoreRosa ++;
                squadre[selezione].budget -= squadre[selezione].nomiGiocatori[contatoreInterno [selezione-1]].prezzo;
            }
            
            if (contatoreRosa == 25 * numPartecipanti)
            {
                azione = 1;
            }
    }
    
    fPtr = fopen ("asta.txt", "a");
    
    if (fPtr == NULL)
    {
         printf ("Errore di apertura del file\n");
         fflush(stdout); 
    }
    
    for (i=0; i < numPartecipanti; i++)
    {
        fprintf (fPtr, "%d. %s\n\n", squadre[i].numG, squadre[i].nomeAllenatore);
        
        for (j=0; j < 25; j++)
        {
            fprintf (fPtr, "%s, %d crediti\n", squadre[i]. nomiGiocatori[j].nomeGiocatore, squadre[i]. nomiGiocatori[j].prezzo);
        } 
            
        fprintf (fPtr, "Budget residuo: %d crediti\n\n", squadre[i].budget);
        
    }    
    
    fclose (fPtr);
    
    printf ("Le modifiche sono state salvate nel file\n");
    fflush(stdout); 
    
    system ("PAUSE");
    return 0;
    
}
    
    
    
    
    
    
    
    
            
            
            
            
          
          
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
