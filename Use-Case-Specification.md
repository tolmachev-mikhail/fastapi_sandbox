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
* Has access to API
### Interaction with the system
* Can register client as a patient
* Can submit a new analysis


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
  * The registrar submits new analysis for the patient

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