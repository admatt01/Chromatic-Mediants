# Chromatic Mediants
 This is a simple python/flask application for creating chromatic mediants and submediants from any musical scale.
 Chromatic mediants are a chord type (triad) that are based on the mediant and submediant triad of a major or minor scale. The mediant and submediant are the third and sixth triad respectively of the diatonic scale. Diatonic simmply means following the natural progression of the scale without altering the natural pattern in any way.

 A chromatic mediant is derived from altering the mediant (third triad) in the scale by changing one or two notes of the mediant while leaving one note unchanged with the result that the new triad will be "chromatic" rather than diatonic, meaning that it does not belong in the natural progression of the scale. Why do this? It is commonly applied to create a sense of tension, expectation, adventure, the unknown etc and is especially popular with cinematic film scores. If you listen to the soundtrack of Lord of the Rings you will hear many examples of chromatic mediants being used.

 Since I am a low-coder/no-coder, the application itself was developed mostly by ChatGPT, first as a standalone python app and then into flask for deployment as a simple web application. If you are new to trying to code with ChatGPT you will quicky find it's no panacea for developing applications, especially ones such as music where the some of the rules can appear ambiguous. In some cases it might be quicker to learn how to actually code rather than wait until ChatGPT gets it right!

 After quite a few hours of careful questioning and refinement plus some debugging and basic modification of the code myself, the application was finally produced.

 I have also ported the application to AWS Lambda as a serverless app which is a quite straightforward process if you have an AWS account and are familiar with Zappa. You can try the application and see how it works by going to https://sr8t5b7hac.execute-api.ap-southeast-4.amazonaws.com/dev. The application usage is basic and self-explanatory.
