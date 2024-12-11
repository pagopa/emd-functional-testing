#language: it
@tpp
Funzionalità: Gestione tpp

    @inserimento
    Scenario: Onboarding multiplo di una TPP
        Dato un payload TPP valido
        Quando invio la richiesta di creazione
        Allora lo stato della risposta deve essere 200
        E la risposta deve essere idempotente