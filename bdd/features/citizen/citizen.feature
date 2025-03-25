@citizen
Feature: Citizen

    Scenario: Onboard user not already onboarded
        Given citizenB never onboarded
        When an onboarding for citizenB on TppFakeEntityIdA request arrives
        Then the creation request is successful
        And others onboarding are not visible

    Scenario: Onboard user already onboarded on the tpp
        Given citizenB already onboarded on TppFakeEntityIdA
        When an onboarding for citizenB on TppFakeEntityIdA request arrives
        Then the creation request is idempotent
        And others onboarding are not visible

    Scenario: Onboard user already onboarded on another tpp
        Given citizenB onboarded on TppFakeEntityIdA and not on TppFakeEntityIdB
        When an onboarding for citizenB on TppFakeEntityIdB request arrives
        Then the creation request is successful
        And others onboarding are not visible

    Scenario: User user not already onboarded
        Given citizenC never onboarded
        When a state change for citizenC on TppFakeEntityIdA request arrives
        Then the state change request fail

    Scenario: User not onboarded on the tpp
        Given citizenC not onboarded on TppFakeEntityIdC
        When a state change for citizenC on TppFakeEntityIdC request arrives
        Then the state change request fail

    Scenario: User onboarded want to disable consent
        Given citizenA already onboarded on TppFakeEntityIdB
        When a state change for citizenA on TppFakeEntityIdB request arrives
        Then the state change request is successful
        And others onboarding are not visible

    Scenario: Tpp onboarded
        Given TppFakeEntityIdA is a valid tpp
        And  citizenA already onboarded on TppFakeEntityIdA
        When a get citizens onboarded list for TppFakeEntityIdA request arrives
        Then the get citizens onboarded list request is successful
        And the tpp consents list is not empty
        And only the tpp enabled consent are visible

    Scenario: User not already onboarded
        Given citizenD never onboarded
        When a get consent state for citizenD and TppFakeEntityIdA request arrives
        Then the get consent state request fail

    Scenario: User not onboarded on the tpp
        Given citizenA not onboarded on TppFakeEntityIdC
        When a get consent state for citizenA and TppFakeEntityIdC request arrives
        Then the get consent state request fail

    Scenario: User onboarded on the tpp
        Given citizenA already onboarded on TppFakeEntityIdA
        When a get consent state for citizenA and TppFakeEntityIdA request arrives
        Then the get consent state request is successful
        And others onboarding are not visible

    Scenario: User not already onboarded
        Given citizenD never onboarded
        When a get consents list for citizenD request arrives
        Then the get consents list request fail

    Scenario: User onboarded
        Given citizenA already onboarded on TppFakeEntityIdA
        When a get consents list for citizenA request arrives
        Then the get consents list request is successful
        And the consents list is not empty

    Scenario: User not already onboarded
        Given citizenD never onboarded
        When a get consents list enabled for citizenD request arrives
        Then the get consents list enabled request fail

    Scenario: User onboarded
        Given citizenA already onboarded on TppFakeEntityIdA
        When a get consents list enabled for citizenA request arrives
        Then the get consents list enabled request is successful
        And the consents list is not empty
        And all the consents are enabled

    Scenario: User onboarded but no enabled consents
        Given citizenC onboarded on TppFakeEntityIdA but disabled
        When a get consents list enabled for citizenC request arrives
        Then the get consents list enabled request is successful
        And the consents list is empty