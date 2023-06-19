# Chromatic Mediants
 This is a simple python/flask application for creating chromatic mediants and submediants from any musical scale.
 Chromatic mediants are a chord type (triad) that are based on the mediant and submediant triad of a major or minor scale. The mediant and submediant are the third and sixth triad respectively of the diatonic scale. Diatonic simply means following the natural progression of the scale without altering the natural pattern in any way.

 A chromatic mediant is derived from altering the mediant (third triad) in the scale by changing one or two notes of the mediant while leaving one note unchanged with the result that the new triad will be "chromatic" rather than diatonic, meaning that it does not belong in the natural progression of the scale. A chromatic submediant is basically the same thing but applied to the sixth triad in the scale progression. Why do this? It is commonly applied to create a sense of tension, expectation, adventure, the unknown etc and is especially popular with cinematic film scores. If you listen to the soundtrack of Lord of the Rings you will hear many examples of chromatic mediants being used.

 Since I am a low-coder/no-coder, the application itself was developed mostly in conjunction with ChatGPT, first as a standalone python app and then into flask for deployment as a simple web application. If you are new to trying to code with ChatGPT you will quicky find it's no panacea for developing applications, especially ones such as music where the some of the rules can appear ambiguous. In some cases it might be quicker to learn how to actually code rather than wait until ChatGPT gets it right!  After quite a few hours of careful questioning and gently coaching ChatGPT, plus a little debugging and basic modification of the code myself, the application was finally produced.

 
Installing and running the code:
 
 - The directory structure is preserved for running as a flask app on port 8080 (can be easily changed by editing the python file). Once you have Flask installed all you should need to do is clone the mediants-v1 folder and its contents into your virtualenv and run the application with "python chromatic-mediants-flask-v1.py &" and browse to http://localhost:8080.

 The only dependencies to run the code as a standalone app are Python3 and Flask. I have also included the standalone python code for usage directly from the command line which is verified on Ubuntu LTS but should work on any OS in a python3 environment.

 I have also ported the application to AWS Lambda as a serverless app which is a quite straightforward process if you have an AWS account and are familiar with Zappa. You can try the application and see how it works by going to https://sr8t5b7hac.execute-api.ap-southeast-4.amazonaws.com/dev. The application usage is basic and self-explanatory.

To Do's:
 - Format into a table style layout to make it look a little prettier.
 - Add 7th's, 9th's and maybe 11th's to the chromatic mediants. Shouldn't be too difficult as the chromatic scale and scale interval tuples are already in place to iterate through.
