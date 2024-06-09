<script setup lang="ts">
    import { toast } from 'vue3-toastify';
    const { signUp } = useAuth();

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
        password: '',
        first_name: '',
        last_name: ''
    });

    const createUser = () => {
        if (credentials.password && credentials.username && credentials.first_name && credentials.last_name) {
            signUp(credentials, { redirect:false })
            .then(() => {
                toast(`User successfully created!`, {
                    theme: 'light',
                    type: 'success',
                    transition: 'slide',
                    dangerouslyHTMLString: true,
                    autoClose: 1500,
                    onClose: () => navigateTo('/')
                });
            })
            .catch((err: any) => {
                if(err.message.includes('400')) {
                    toast(`User already exists`, {
                        theme: 'light',
                        type: 'error',
                        transition: 'slide',
                        dangerouslyHTMLString: true
                    });
                } else if(err.message.includes('<no response>')) {
                    toast(`Not possible to connect with the server`, {
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

    const loginPage = () => {
        navigateTo('/user/login');
    }
</script>

<template>
    <main class="flex align-center justify-center items-center">
        <section class="flex w-3/5 h-[70%] rounded-2xl">
            <div class="bg-black w-3/5 h-full rounded-l-2xl flex items-center justify-center">
                <div class="flex flex-col items-center justify-evenly w-full h-[70%]">
                    <h1 class="text-pink-default font-bold text-[50px] w-full text-center">Welcome to our family!</h1>
                    <div class="flex flex-col w-1/2 items-start">
                        <label for="username" class="text-white font-bold mb-1">
                            Username *
                        </label>
                        <div class="flex justify-center w-full">
                            <input id="username" type="text" v-model="credentials.username"
                                class="h-[50px] w-full rounded-lg bg-beige px-4 outline-none font-medium" />
                        </div>
                    </div>

                    <div class="flex flex-row w-full items-center justify-center">
                        <div class="flex flex-col w-[24%] items-start">
                            <label for="first_name" class="text-white font-bold mb-1">
                                First Name *
                            </label>
                            <div class="flex justify-center w-full">
                                <input id="first_name" type="text" v-model="credentials.first_name"
                                    class="h-[50px] w-full rounded-lg bg-beige px-4 outline-none font-medium" />
                            </div>
                        </div>

                        <div class="flex flex-col w-[24%] items-start ml-[2%]">
                            <label for="last_name" class="text-white font-bold mb-1">
                                Last Name *
                            </label>
                            <div class="flex justify-center w-full">
                                <input id="last_name" type="text" v-model="credentials.last_name"
                                    class="h-[50px] w-full rounded-lg bg-beige px-4 outline-none font-medium" />
                            </div>
                        </div>
                    </div>

                    <div class="flex flex-col w-1/2 items-start">
                        <label for="password" class="text-white font-bold mb-1">
                            Password *
                        </label>
                        <div class="flex justify-center w-full">
                            <input id="password" type="password" v-model="credentials.password"
                                class="h-[50px] w-full rounded-lg bg-beige px-4 outline-none font-medium" />
                        </div>
                    </div>

                    <Button @click="createUser"
                        class="text-white font-bold bg-pink-default w-1/2 h-[50px] rounded-lg">
                        Create your Account
                    </Button>
                </div>
            </div>
            <div class="bg-beige w-2/5 h-full rounded-r-2xl flex items-center justify-center">
                <div class="flex flex-col justify-evenly items-center w-full h-3/5">
                    
                    <img src="~/public/book_image.png" class="w-4/5" />

                    <Button
                        @click="loginPage"
                        class="text-white font-bold bg-black w-1/2 h-[50px] rounded-lg"
                    >
                        Login in your Account
                    </Button>
                </div>
            </div>
        </section>
    </main>
</template>