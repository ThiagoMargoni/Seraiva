<script setup lang="ts">
    import { toast } from 'vue3-toastify';
    const { signIn } = useAuth();

    definePageMeta({
        layout: 'login',
        middleware: 'auth',
        auth: {
            unauthenticatedOnly: true,
            navigateAuthenticatedTo: '/'
        }
    });
            
    const credentials = reactive({
        username: '',
        password: ''
    });

    const submitLogin = () => {
        if (credentials.password && credentials.username) {
            signIn(credentials, { redirect:false })
            .then(() => {
                navigateTo('/');
            })
            .catch((err: Error) => {
                console.log(err.message)
                if(err.message.includes('<no response>')) {
                    toast(`Not possible to connect with the server`, {
                        theme: 'light',
                        type: 'error',
                        transition: 'slide',
                        dangerouslyHTMLString: true
                    });
                } else if(err.message.includes('400')) {
                    toast(`User/Password Mismatch`, {
                        theme: 'light',
                        type: 'error',
                        transition: 'slide',
                        dangerouslyHTMLString: true
                    });
                } else {
                    toast(`An error ocurred`, {
                        theme: 'light',
                        type: 'error',
                        transition: 'slide',
                        dangerouslyHTMLString: true
                    });
                }
            });
        } else {
            toast('Please fill all fields before continuing!', {
                theme: 'light',
                type: 'warning',
                transition: 'slide',
                dangerouslyHTMLString: true
            });
        }
    }

    const signupPage = () => {
        navigateTo('/user/signup')
    }
</script>

<template>
    <div class="flex align-center justify-center items-center w-screen">
        <section class="flex w-3/5 h-[70%] rounded-2xl">
            <div class="bg-black w-3/5 h-full rounded-l-2xl flex items-center justify-center">
                <div class="flex flex-col items-center justify-evenly w-full h-[70%]">
                    <h1 class="text-pink-default font-bold text-[50px] w-full text-center">Welcome Back!</h1>
                    <div class="flex flex-col w-1/2 items-start">
                        <label for="username" class="text-white font-bold mb-1">
                            Username
                        </label>
                        <div class="flex justify-center w-full">
                            <input id="username" type="text" v-model="credentials.username"
                                class="h-[50px] w-full rounded-lg bg-beige px-4 outline-none font-medium" />
                        </div>
                    </div>

                    <div class="flex flex-col w-1/2 items-start">
                        <label for="password" class="text-white font-bold mb-1">
                            Password
                        </label>
                        <div class="flex justify-center w-full">
                            <input id="password" type="password" v-model="credentials.password"
                                class="h-[50px] w-full rounded-lg bg-beige px-4 outline-none font-medium" />
                        </div>
                    </div>

                    <Button @click="submitLogin"
                        class="text-white font-bold bg-pink-default w-1/2 h-[50px] rounded-lg">
                        Login
                    </Button>
                </div>
            </div>
            <div class="bg-beige w-2/5 h-full rounded-r-2xl flex items-center justify-center">
                <div class="flex flex-col justify-evenly items-center w-full h-[30%]">
                    <div class="flex flex-row w-3/5 justify-evenly mb-0.5">
                        <div class="text-2xl cursor-pointer">
                            <i class="pi pi-google"></i>
                        </div>
                        <div class="text-2xl cursor-pointer">
                            <i class="pi pi-facebook"></i>
                        </div>
                        <div class="text-2xl cursor-pointer">
                            <i class="pi pi-twitter"></i>
                        </div>
                        <div class="text-2xl cursor-pointer">
                            <i class="pi pi-discord"></i>
                        </div>
                    </div>
                    <hr class="w-[80%]">
                    <Button 
                        @click="signupPage"
                        class="text-white font-bold bg-black w-1/2 h-[50px] rounded-lg"
                    >
                        Create an Account
                    </Button>
                </div>
            </div>
        </section>
    </div>
</template>