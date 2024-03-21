## Actor: Client
### Description: A requester analysis and can be registered in database as a patient
### Characteristics:
* Has properties that can be verified
  * Name
  * Surname
  * Gender
  * Date of Birth
  * Passport ID
  * Email

* Has access to API
* Can request an analysis via Register
### Interaction with the system
* Can obtain analysis result by analysis ID
* Can get his analysis history

## Actor: Receptionist
### Description: A worker that can register a patient and submit new analysis request
### Characteristics:
* Has properties that can be verified
  * Corporate Email
  * Password
### Interaction with the system
* Can register client as a patient
* Can submit a new analysis
* Can update information about patient

## Actor: Laboratory Assistant
### Description: A worker that actually runs analysis
### Characteristics:
* Has properties that can be verified
  * Corporate Email
  * Password
### Interaction with the system
  * Can get analysis result

## Actor: Doctor
### Description: A worker that verifies analysis result
### Characteristics:
* Has properties that can be verified
  * Corporate Email
  * Password
### Interaction with the system
  * Can get analysis result
  * Can update analysis result


# Client requests analysis

* Description Client requests analysis
* Actors: Client, Receptionist, registry API
* Preconditions:
  * Client respects the analysis precondition guidelines
  * Client has valid passport
* Flow:
  * Receptionist manually validates client passport
  * Receptionist searches for a client in database using API endpoint and catches Exception
  * Receptionist registers the client as patient using API endpoint
  * Receptionist collects payment via cash or any third party provider (credit card, QR code etc)
  * Receptionist submits new analysis using API

* Alternative flow:
  * Receptionist manually validates client passport
  * Receptionist search for a client using API endpoint and finds patient
  * Receptionist collects payment via cash or any third party provider (credit card, QR code etc)
  * Receptionist submits new analysis for the patient

* Exceptions:
  * Analysis is not available


# New patient registration

* Description: Receptionist registers a new patient
* Actors: Client, Receptionist, registry API
* Preconditions:
  * Client has valid passport
* Flow: 
  * Receptionist manually validates patient passport
  * Receptionist submits name, surname, gender, date of birth, passport ID via registry API
* Exceptions:
  * Client has already been registered before

# Search for a patient

* Description: Receptionists searches for a client as a laboratory patient
* Actors: Client, Receptionist, registry API
* Preconditions:
  * Client has valid passport
* Flow:
  * Receptionist manually validates clients passport
  * Receptionist searches for a database entry via registry API
* Exceptions:
  * No patient found

# Login to system

* Description: User logins using credential pair (email and password) and provide authorization information by selecting scope
* Actors: Client, Receptionist, Doctor, Laboratory Assistant
* Preconditions:
  * Client was registered in system
* Flow:
  * User provides credential pair and desired list of scopes
  * System validates credentials and filters list of scopes based on available scope for user
  * System generates access token that could be used for authentication and authorization
* Exceptions:
  * Credential pair was not found in database
  * User has no right to ges selected scopes 