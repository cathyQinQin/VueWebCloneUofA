<template>
    <div class="banner-container">
        <a href="index.html" class="banner">
            <img alt="ualberta" src="https://www.ualberta.ca/media-library/ualberta-logo-reverse.svg">
        </a>
        <ul>
            <li>
                <a href="https://www.ualberta.ca/admissions-programs/index.html">Prospective Students</a>
            </li>
            <li>
                <a href="https://www.ualberta.ca/current-students">Current Students</a>
            </li>
            <li>
                <a href="https://www.ualberta.ca/faculty-and-staff">Faculty &amp; Staff</a>
            </li>
            <li>
                <a href="https://www.ualberta.ca/alumni">Alumni &amp; Friends</a>
            </li>
        </ul>
    </div>
</template>
<style scoped>
.banner-container {
    background: #007c41 url(https://www.ualberta.ca/media-library/banner-bg.svg);
    height: 6.42857em;
    border-bottom: 3px solid #ffdb05;
    color: #fff;
    display: flex;
    justify-content: space-between;
    padding: 0 8%;
    }
.banner-container ul li>a {  
    font-family: "DIN Bold", sans-serif;
    font-size: 13px;
    font-weight: 600;
    text-decoration: none;
    color: #fff;
    margin-left: 5px;
}
img {
    width: 241.5px;
    height: 72px;
    margin-top: 18px;
}
ul {
    display: flex;
    list-style: none;
    align-items: flex-end;
    margin-bottom: 1%;
}
ul > li {
    padding: 0 10px;
}
</style>