<template>
<footer data-aos="fade-up" class="bg-primary-gradient">
    <div class="container py-4 py-lg-5">
        <div class="row justify-content-center">
            <div class="col-lg-3 text-center text-lg-start d-flex flex-column align-items-center order-first align-items-lg-start order-lg-last">
                <div class="fw-bold d-flex align-items-center mb-2"><span class="bs-icon-sm bs-icon-circle bs-icon-primary d-flex justify-content-center align-items-center bs-icon me-2" style="width: 70px;height: 70px;"><img width="48" height="41" src="https://elasticbeanstalk-eu-west-3-625039870308.s3.eu-west-3.amazonaws.com/img/logo-nobg.png" style="text-align: center;height: 50px;width: 50px;margin: 0px;padding: 0px;margin-top: -6px;margin-right: -1px;"></span><span style="font-weight: bold;font-size: 22px;padding: 0px;margin-right: 0px;margin-left: 14px;">LEARN WITH PIMA</span></div>
                <p class="text-muted" style="font-style: italic;"><br>Learn with Pima is a student project that tries to incorporate flashcards for learning such as websites like Quizlet.</p>
            </div>
            <div class="col-sm-4 col-md-3 text-center text-lg-start d-flex flex-column">
                <h3 class="fs-6 fw-bold">Collaborators</h3>
                <ul class="list-unstyled">
                    <li><a href="#">THUO Menghor</a></li>
                    <li><a href="#">DESPREZ Mathieu</a></li>
                    <li><a href="#">NOUV Ratanakmuny</a></li>
                    <li><a href="#">GORGI Skander</a></li>
                    <li><a href="#">THAY Ugo</a></li>
                    <li><a href="#">ZHANG Xichen</a></li>
                </ul>
            </div>
            <div class="col-sm-4 col-md-3 col-xxl-4 text-center text-lg-start d-flex flex-column">
                <h3 class="fs-6 fw-bold">Tools</h3>
                <ul class="list-unstyled">
                    <li><a href="#">• Backend : Python (Flask JSON Restful API)<br><br></a></li>
                    <li><a href="#">• Frontend : Javascript (Vue 3 Framework)<br><br></a></li>
                    <li><a href="#">• Hosting : Amazon Web-Services free tier :<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;- VPS for backend + frontend<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;- RDP with mysql for the database<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;- CDN for media content<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;- Domain from www.one.com</a></li>
                </ul>
            </div>
        </div>
        <hr>
        <div class="text-muted d-flex justify-content-between align-items-center pt-3">
            <p class="mb-0" style="font-style: italic;">Learn With Pima - 2023</p>
            <ul class="list-inline mb-0">
                <li class="list-inline-item"></li>
                <li class="list-inline-item"></li>
                <li class="list-inline-item"></li>
            </ul>
        </div>
    </div>
</footer>
</template>
<script>
    export default {
      name: 'FooterComponent'
    };
</script>