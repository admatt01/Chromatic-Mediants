# Chromatic Mediants
This is a simple python/flask, serverless application for creating chromatic mediants and submediants from any musical scale.
Chromatic mediants are a chord type (triad) that are based on the mediant and submediant triad of a major or minor scale. The mediant and submediant are the third and sixth triad respectively of the diatonic scale. Diatonic simply means following the natural progression of the scale without altering the natural pattern in any way.

As well as printing the mediants and classical chromatic mediants for any Major or Minor scale, the application also includes audio samples for chromatic mediants and submediants in the key of C Major and C Minor to give you an idea of how the mediants sound and their effect.

A chromatic mediant is derived from altering the mediant (third triad) in the scale by changing one or two notes of the mediant while leaving one note unchanged with the result that the new triad will be "chromatic" rather than diatonic, meaning that it does not belong in the natural progression of the scale. A chromatic submediant is basically the same thing but applied to the sixth triad in the scale progression. Why do this? It is commonly applied to create a sense of tension, expectation, adventure, the unknown etc and is especially popular with cinematic film scores. If you listen to the soundtrack of Lord of the Rings you will hear many examples of chromatic mediants being used.

Since I am a low-coder/no-coder, the application itself was developed mostly in conjunction with ChatGPT, first as a standalone python app and then into flask for deployment as a serverless application on AWS Lambda. If you are new to trying to code with ChatGPT you will quicky find it's no panacea for developing applications, especially ones such as music where the some of the rules can appear ambiguous. In some cases it might be quicker to learn how to actually code rather than wait until ChatGPT gets it right!  After quite a few hours of careful questioning and gently coaching ChatGPT, plus a little debugging and basic modification of the code myself, the application was finally produced.

 
Installing and running the code:
 
- You will need Python3, Flask, Zappa and an AWS account.
  - Make sure your workstation has Python3.9 installed
  - Clone or download and tar/unzip the code to your machine
  - cd into the mediants-v1 project folder
  - Setup your environment (pipenv install)
  - Install Flask (pipenv install flask)
  - Install Zappa (pipenv install zappa)

Log into your AWS account and setup a user with sufficient privileges for a Zappa serverless deployment (plenty of info available via Google on how to do this) and download your access and secret access key. Create a credentials file in your /home/.aws directory and enter your access and secret key details and run 'zappa init'. This will setup the json file for your Lambda deployment and you will then need to edit the init file created for inclusion of your AWS region to suit whatever region you would like to deploy into. Once you have made and saved your changes run 'zappa deploy dev'. The files will upload to AWS Lambda and create the application resulting in an endpoint you can browse to for testing. There should be no cost since AWS Lambda is included in the AWS Free-Tier.

To Do's:
 - Add 7th's, 9th's and maybe 11th's to the chromatic mediants. Shouldn't be too difficult as the chromatic scale and scale interval tuples are already in place to 
 iterate through.
