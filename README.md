# [Ombudsman](https://ombudsman.user.camp) by [User Camp](https://user.camp)

Ombudsman is a Zapier integration that sends triggers whenever new data is available in your Windows Dev Center.

## Usage

Go to [https://ombudsman.user.camp](https://ombudsman.user.camp) to generate a User Camp API key.

Your Windows Developer account needs to be associated with an Azure AD that you are an admin of. You need to create an Azure
AD Application.

You need to join the [private Ombudsman Zapier application](https://zapier.com/developer/invite/61854/389dc5ae8662f71159d766f347d8ad2c/).

Full setup docs available at https://ombudsman.user.camp .

## Deploying it yourself

Ombudsman is built with Django and is meant to be deployed on Heroku.

To deploy Ombudsman yourself, make sure you have the following enviornment variables set:

- `OMBUDSMAN_DJANGO_SECRET_KEY`
- `OMBUDSMAN_ROLLBAR_ACCESS_TOKEN`, a token from [Rollbar](https://rollbar.com), used for error reporting
- `OMBUDSMAN_SENDGRID_USERNAME` from [Sendgrid](http://sendgrid.com/), used for sending out API keys
- `OMBUDSMAN_SENDGRID_PASSWORD`
- `OMBUDSMAN_RECAPTCHA_PUBLIC_KEY` from [reCAPTCHA](https://www.google.com/recaptcha/intro/invisible.html), for preventing abuse of the API signup form
- `OMBUDSMAN_RECAPTCHA_PRIVATE_KEY`

## License

(MIT)

Copyright (c) 2017 User Camp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
