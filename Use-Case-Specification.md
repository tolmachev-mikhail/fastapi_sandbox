# Client requests analysis

* Description Client requests analysis
* Actors: Client, Passport, Receptionist, Patient, registry API
* Preconditions:
  * Patient respect the analysis precondition guidelines
  * Patient has valid passport
* Flow:
  * Receptionist manually validates patient passport
  * Receptionist searches for a client in database using API endpoint and catches Exception
  * The registrar registers the client using API endpoint
  * Receptionist collects payment via cash or any third party provider (credit card, QR code etc)
  * The registrar submits new analysis using API

* Alternative flow:
  * Receptionist manually validates patient passport
  * Receptionist search for a patient using API endpoint and finds patient
  * Receptionist collects payment via cash or any third party provider (credit card, QR code etc)
  * The registrar submits new analysis for the patient

* Exceptions:
  * Analysis is not available


# New patient registration

* Description: Receptionist registers a new patient
* Actors: Client, Passport, Receptionist, Patient, registry API
* Preconditions:
  * Client has valid passport
* Flow: 
  * Receptionist manually validates patient passport
  * Receptionist submits name, surname, gender, date of birth, passport ID via registry API
* Exceptions:
  * Client has already been registered before

# Search for a patient

* Description: Receptionists searches for a client as a laboratory patient
* Actors: Client, Passport, Receptionist, Patient, registry API
* Preconditions:
  * Client has valid passport
* Flow:
  * Receptionist manually validates patient passport
  * Receptionist searches for a client database entry via registry API
* Exceptions:
  * No patient found