<template>
<div class="footer">
    <div class="new-quick-links">
        <div class="quick-link">
            <ul>
                <li>
                    <strong>About Us</strong>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/about/contact">Contact Us</a>
                </li>
                <li>
                    <a href="https://www.careers.ualberta.ca/">Careers</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/news-and-events/mediarelations">Media Relations</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/president">President</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/about/leadership">Leadership</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/governance">Governance</a>
                </li>
                <li>
                    <a href="https://policiesonline.ualberta.ca/">Policies</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/privacy">Privacy Statement</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/faculty-and-staff/pay-tax-information/compensation-disclosure">Compensation Disclosure</a>
                </li>
            </ul>
        </div>
        <div class="quick-link">
            <ul>
                <li>
                    <strong>Student Information</strong>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/registrar">Registrar</a>
                </li>
                <li>
                    <a href="https://www.su.ualberta.ca/">Student Union</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/graduate-students-association">Grad Students</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/provost/dean-of-students">Dean of Students</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/current-students/accessibility-resources">Accessibility</a>
                </li>
            </ul>
        </div>
        <div class="quick-link">
            <ul>
                <li>
                    <strong>Campus Info</strong>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/maps">Locations</a>
                </li>
                <li>
                    <a href="https://www.library.ualberta.ca/">Libraries</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/dining-services">Dining Services</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/parking-services">Parking</a>
                </li>
                <li>
                    <a href="https://ist.ualberta.ca/">IT Help</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/museums">Museums</a>
                </li>
                <li>
                    <a href="https://www.ualberta.ca/emergency.html">Emergency</a>
                </li>
            </ul>
        </div>
        <div class="quick-link" id="colWeather">
            <div class="weather">
                <div class="img-wrapper">
                    <img src="https://www.ualberta.ca/media-library/weather-icons/partly-cloudy-day.svg" alt="Partly Cloudy">
                </div>
                <div class="current-temp">
                    <div class="temp">{{weatherTemp}}°C</div>
                    <div class="feels-like">Feels like {{weatherFeel}}°C</div>
                </div>
            </div>
            <div class="weather-name">{{weatherDescription}}</div>
            <a href="https://weather.gc.ca/city/pages/ab-50_metric_e.html" target="_blank">
                <div><span>Edmonton Full Forecast »</span></div>
            </a>
            <div class="powered-by">
                <a href="https://openweathermap.org/api" target="_blank">Powered by OpenWeather</a>
            </div>
        </div>
    </div>
    <div class="footer-address">
		<p>
			<span>©2021 University of Alberta 116 St. and 85 Ave., Edmonton, AB, Canada T6G 2R3
			</span>
			<span>We are located on Treaty 6 / Métis Territory.</span>
		</p>
	</div>
    <input v-model="message" placeholder="edit me" />
    <p>Message is: {{ message }}</p>
    <button @click="submit">
    <slot>Submit</slot>
    </button>
</div>  
</template>
<script>
import axios from 'axios'
import {ref} from 'vue'
export default {
    async setup() {
        let datas = [];
        await axios.get('http://api.openweathermap.org/data/2.5/weather?id=5946768&appid=028c10f9b44897f8efe7bfdf9d2af33a').then((res) => {
            datas = res.data;
        });
        const kelvin = 273.15;
        const weatherTemp = ref(parseInt(datas.main.temp - kelvin));
        const weatherDescription = ref(datas.weather[0].description);
        const weatherFeel = ref(parseInt(datas.main.feels_like - kelvin));
        const message = ref('');
        function submit() {
                    //向服务器提交数据
                    axios.get('http://127.0.0.1:3000/')
                        .then(function(response) {
                            //成功时服务器返回 response 数据
                            alert(response.data)
                        })
                        .catch(function(error) {
                            console.log(error);
                        });
                }
        return{
            weatherTemp,
            weatherDescription,
            weatherFeel,
            message,
            submit
        }
    },
}
</script>
<style scoped>
    .footer{
        background-color:#2E6A3B;
        color:#fff;
    }
    .footer a{
        color:#fff;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .new-quick-links{
        display: flex;
        padding-top: 40px;
        border-top: 1px solid #ddd;
        margin: 0 8%;
    }
    .quick-link{
        flex: 0 0 25%;
    }
    .new-quick-links ul{
        list-style: none; 
    }
    .new-quick-links ul a:hover {
        text-decoration: underline;
    }
    .weather{
        display: flex;
        align-items: flex-end;
    }
    .weather .img-wrapper{
        flex: 0 0 30%;
        margin-right: 5%;
    }
    .weather div{
        flex: 0 0 70%;
    }
    .weather .current-temp .temp{
        font-family: 'DIN BOLD', sans-serif;
        font-size: 2em;
    }
    .weather-name{
        font-family: 'DIN BOLD', sans-serif;
        margin-top: 10px;
        font-size: 1.5em;
    }
    .footer-address{
        border-top: 1px solid #ddd;
        margin: 0 8%;
        padding: 5% 0;
    }
</style>