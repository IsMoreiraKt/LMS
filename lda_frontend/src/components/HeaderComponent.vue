<template>
    <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start px-5">
        <a href="/" class="p-3 d-flex flex-column align-items-center navbar-brand my-2 my-lg-0 me-lg-auto text-white text-decoration-none">
            <svg fill="#ffffff" height="24px" width="24px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier"> 
                    <g> <g> 
                        <path d="M425.918,325.916c-32.008-32.008-71.46-53.858-114.447-63.969l-28.001,28.001l12.271,148.575 c0.416,5.041-0.957,10.066-3.879,14.194l-27.999,39.563c-1.806,2.552-4.739,4.07-7.866,4.07c-3.127,0-6.06-1.518-7.866-4.07 l-27.999-39.563c-2.921-4.128-4.295-9.154-3.879-14.194l12.271-148.576l-28.001-28.001 c-42.987,10.111-82.439,31.96-114.447,63.969c-45.387,45.387-70.383,105.733-70.383,169.921c0,8.927,7.237,16.164,16.164,16.164 h448.28c8.927,0,16.164-7.237,16.164-16.164C496.302,431.648,471.305,371.303,425.918,325.916z"></path> 
                    </g> </g> 
                    <g> <g> 
                        <path d="M383.757,40.025c-2.376-0.794-4.993,0.02-6.499,2.021l-41.997,55.796L258.091,2.168C256.985,0.796,255.319,0,253.558,0 c-1.76,0-3.427,0.796-4.533,2.168l-77.169,95.674L134.78,47.334c-1.49-2.03-4.115-2.872-6.507-2.088 c-2.392,0.784-4.011,3.016-4.011,5.534v87.038h263.472v-92.27C387.734,43.043,386.132,40.819,383.757,40.025z"></path> 
                    </g> </g> 
                    <g> <g> 
                        <path d="M124.261,170.147v32.318c0,7.166,5.809,12.975,12.976,12.975h237.522c7.166,0,12.975-5.809,12.975-12.975v-32.318H124.261 z"></path> 
                    </g> </g> 
                </g>
            </svg>
            <span class="text-center c-small text-white mt-2">LDA Vue Edition</span>
        </a>


        <ul class="nav col-12 col-lg-auto my-2 justify-content-center my-md-0 text-small">
            <li>
                <a href="#" 
                class="nav-link d-flex flex-column align-items-center text-decoration-none" 
                :class="{'text-secondary': activeItem === 'home', 'text-white': activeItem !== 'home'}"
                @click="setActiveItem('home')"
                >
                    <i class="bi bi-house mb-1" style="font-size: 24px;"></i>
                    <span>Home</span>
                </a>
            </li>

            <li>
                <a href="#" 
                class="nav-link d-flex flex-column align-items-center text-decoration-none" 
                :class="{'text-secondary': activeItem === 'dashboard', 'text-white': activeItem !== 'dashboard'}"
                @click="setActiveItem('dashboard')"
                >
                    <i class="bi bi-speedometer2 mb-1" style="font-size: 24px;"></i>
                    <span>Dashboard</span>
                </a>
            </li>

            <li>
                <a href="#" 
                class="nav-link d-flex flex-column align-items-center text-decoration-none" 
                :class="{'text-secondary': activeItem === 'orders', 'text-white': activeItem !== 'orders'}"
                @click="setActiveItem('orders')"
                >
                    <i class="bi bi-table mb-1" style="font-size: 24px;"></i>
                    <span>Orders</span>
                </a>
            </li>

            <li>
                <a href="#" 
                class="nav-link d-flex flex-column align-items-center text-decoration-none" 
                :class="{'text-secondary': activeItem === 'products', 'text-white': activeItem !== 'products'}"
                @click="setActiveItem('products')"
                >
                    <i class="bi bi-grid mb-1" style="font-size: 24px;"></i>
                    <span>Products</span>
                </a>
            </li>

            <li>
                <a href="#" 
                class="nav-link d-flex flex-column align-items-center text-decoration-none" 
                :class="{'text-secondary': activeItem === 'customers', 'text-white': activeItem !== 'customers'}"
                @click="setActiveItem('customers')"
                >
                    <i class="bi bi-people mb-1" style="font-size: 24px;"></i>
                    <span>Customers</span>
                </a>
            </li>
        </ul>
    </div>
</template>



<script>
    export default {
        name: 'HeaderComponent',
        data() {
            return {
                activeItem: 'home'
            };
        },
        methods: {
            setActiveItem(item) {
                this.activeItem = item;
            }
        }
    }
</script>



<style>
    .nav-link {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .c-small {
        margin-top: 0.3rem;
    }
</style>