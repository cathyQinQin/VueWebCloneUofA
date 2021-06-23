<template>
    <div class="main-container">
        <div class="study-with-us">
            <h2 class="study-with-us">Study With Us</h2>
            <p class="study-with-us-sub">University of Alberta is a Top 5 Canadian university and one of the Top 150 in the world. Find out what makes our student experience so rich, meaningful and life-changing.</p>
        </div>
        <div class="two-studies">
            <div class="u-study">
                <a aria-label="Graduate Studies" href="https://www.ualberta.ca/admissions/undergraduate"><i aria-hidden="true" class="fas fa-graduation-cap fa-5x"></i></a>
                <h3><a href="https://www.ualberta.ca/admissions/undergraduate">Undergraduate Studies</a></h3>
                <p>Your journey starts here. Choose from more than 200 program options, check the admission requirements, and apply online.</p>
                <ul>
                    <li><a href="http://apps.admissions.ualberta.ca/programs/">Find Your Program »</a></li>
                    <li><a href="https://www.ualberta.ca/admissions/undergraduate/admission">Begin Your Application »</a></li>
                 </ul>
            </div>
            <div class="g-study">
                <a aria-label="Graduate Studies" href="https://www.ualberta.ca/graduate-studies/prospective-students"> <i aria-hidden="true" class="fas fa-book fa-5x"></i> </a>
                <h3><a href="https://www.ualberta.ca/graduate-studies/prospective-students">Graduate Studies</a></h3>
                <p>More than 500 graduate programs, 250 specializations, and 300 research areas - find out how to take your education to the next level.</p>
                <ul>
                    <li><a href="graduate-programs/index.html">Find Your Program »</a></li>
                    <li><a href="https://www.ualberta.ca/graduate-studies/prospective-students/apply-for-admission">Begin Your Application »</a></li>
                </ul>
            </div>
        </div>
        <div class="more-study">
            <h3>More Study Options</h3>
            <div class="contact-container">
            <ul class="contact-list">
                <li><a href="admissions-programs/online-courses/index.html">Online Courses</a></li>
                <li><a href="https://ext.ualberta.ca/">Continuing Education</a></li>
                <li><a href="https://www.ualberta.ca/lougheed-leadership-college/index.html">Leadership Studies</a></li>
            </ul>
            <ul class="contact-list">
                <li><a href="https://ext.ualberta.ca/els">English Language School</a></li>
                <li><a href="https://ext.ualberta.ca/els/bridging-program">Bridging Program</a></li>
                <li><a href="admissions-programs/visiting-student-and-internship-programs/index.html">Visiting Student &amp; Internship Programs</a></li>
            </ul>
            <ul class="contact-list">
                <li><a href="admissions-programs/exchange-programs/index.html">Exchange Programs</a></li>
                <li><a href="https://www.ualberta.ca/registrar/registration-and-courses/special-registrations/open-studies/index.html">Open Studies</a></li>
                <li><a href="admissions-programs/inclusive-education/index.html">Inclusive Education</a></li>
            </ul>
        </div>
    </div>
    </div>
</template>
<style scoped>
    .main-container{
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 0 8%;
        color: rgb(61, 74, 67);
        justify-content: space-between;
        font-weight: 600;
    }
    .main-container a{
        text-decoration: none;
        color: #007c41;
    }
    .main-container a:hover{
        text-decoration: underline;
    }
    .main-container i{
        color: #00402d;
    }
    .main-container ul{
        list-style: none;
    }
    .main-container h3{
        font-size: 1.375rem;
    }
    h2.study-with-us {
        margin-top: 1.5rem;
        padding: 1rem;
        font-size: 2.143rem;
        font-family: 'DIN Bold', sans-serif;
        text-align: center;
        font-weight: 600;
        text-transform: uppercase
    }
    .study-with-us-sub {
        text-align: center;
        font-size: 1.3rem;
        font-family: 'DIN Regular', sans-serif;
        font-weight: 350;
    }
    .two-studies{
        margin-top: 1rem;
        display: flex;
    }
    .two-studies p{
        line-height: 1.3em;
    }
    .u-study, .g-study{
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 2rem 4rem;
    }
    .g-study{
        border-left: 3px dotted #231f20;
        margin-left: 1rem;
    }
    .study-with-us a{
        color: #007c41;
    }
    .two-studies a:hover {
        color: #003019;
        text-decoration: none;
    }
    .more-study{
        margin-top: 3rem;
        width: 100%;
        background: #f5f8f6;
        padding: 40px 30px 40px 30px;
    }
    .contact-container{
        display: flex;
        justify-content: space-around;
    }
    .contact-list{
        flex: 1;
        padding: 0 2rem;
    }
    .contact-list li{
        border-bottom: 1px dotted #e0e0e0;
        padding: .3571em 0;
    }
</style>