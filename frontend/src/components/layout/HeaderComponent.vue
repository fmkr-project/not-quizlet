<template>
    <nav class="navbar navbar-expand-md sticky-top navbar-shrink py-3 navbar-light" data-aos="fade-down" id="mainNav">
      <div class="container">
        <a class="navbar-brand d-flex align-items-center" href="/">
          <span class="bs-icon-sm bs-icon-circle bs-icon-primary shadow d-flex justify-content-center align-items-center me-2 bs-icon" style="width: 100px;height: 100px;">
            <img width="48" height="41" src="https://elasticbeanstalk-eu-west-3-625039870308.s3.eu-west-3.amazonaws.com/img/logo-nobg.png" style="text-align: center;height: 73px;width: 73px;margin: 0px;padding: 0px;margin-top: -6px;margin-right: -1px;">
          </span>
        </a>
        <button data-bs-toggle="collapse" class="navbar-toggler" data-bs-target="#navcol-1">
          <span class="visually-hidden">Toggle navigation</span>
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navcol-1">
          <div class="col-xxl-1">
            <h1 class="fw-bold" style="font-size: 31px;">Polyvalent Interactive <br>Mastery App </h1>
          </div>
          <ul class="navbar-nav mx-auto">
            <li class="nav-item">
              <a class="nav-link active" href="index.html">Home</a>
            </li>
            <li class="nav-item"></li>
            <li class="nav-item">
              <a class="nav-link" href="register.html">Projects</a>
            </li>
            <li class="nav-item"></li>
            <li class="nav-item"></li>
          </ul>
          <small style="margin-right: 70px;">ENG</small>
          <p class="navbar-text p-0 m-0">
            <a href="#"></a>
          </p>
          <a href="#" style="padding: 0px;margin: 10px;text-decoration: underline;margin-right: 16px;">Register</a>
          <a class="btn btn-primary shadow" role="button" href="login.html">Sign in</a>
        </div>
      </div>
    </nav>
  </template>
  <script>
    export default {
      name: 'HeaderComponent'
    };
  </script>
  <style scoped>
    /* You can add scoped CSS styles here, specific to this component */
  </style>