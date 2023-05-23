Vue.component('div class="side-menu-bar"', {
    template: `
        <div class="side-menu-bar">
                    <div class="flex  w-full">
                    <div id="SideMenu" class="side-menu">
                    <div @click="newMessageOpen = true" class="
                        flex
                        items-center
                        justify-center
                        bg-primary-100 w-52 
                        
                        h-20
                        mt-10
                        rounded-2xl
                        ml-5
                        p-7
                        cursor-pointer
                        ">
                        <PencilOutlineIcon :size="27" class="mr-2" />
                        <span class="text-sm font-bold text-primary-600">メール作成</span>
                    </div>

                    <router-link to="/email">
                        <div class="
                            flex
                            justify-center
                            mt-2
                            ml-5
                            mr-5
                            px-8
                            py-3
                            bg-primary-200 hover:bg-primary-500 w-52 h-21
                            rounded-3xl
                        ">


                        <div class="flex items-center"> 
                            <InboxIcon :size="17" />
                            <div class="text-sm pl-4 font-bold text-primary-600 text-align-left">受信箱</div>
                        </div>
                        </div>
                    </router-link>


                    <div class="
                        flex 
                        justify-center 
                        mt-2
                        ml-5
                        mr-5
                        px-8 
                        py-3
                        
                        bg-primary-200 hover:bg-primary-500 w-52 h-21
                        rounded-3xl
                        cursor-pointer
                        ">
                        <div class="flex items-center">
                        <FileOutlineIcon :size="17" />
                        <div class="text-sm pl-5 font-bold text-primary-600">下書き</div>
                        </div>
                    </div>

                    <div
                        class="flex justify-center mt-2 ml-5 px-8 py-3  bg-primary-200 hover:bg-primary-500 w-52 h-21 mr-5 rounded-3xl cursor-pointer">
                        <div class="flex items-center">
                        <SendOutlineIcon :size="17" />
                        <div class="text-sm pl-4 font-bold text-primary-600">送信済み</div>
                        </div>
                    </div>

                    <div
                        class="flex justify-center mt-2 ml-5 mr-5 px-8 py-3  bg-primary-200 hover:bg-primary-500 w-52 h-21 rounded-3xl cursor-pointer">
                        <div class="flex items-center">
                        <TrashCanOutline :size="17" />
                        <div class="text-sm pl-4 font-bold text-primary-600">ゴミ箱</div>
                        </div>
                    </div>

                    <div @click="movealarmScreen" 
                        class="flex justify-center mt-2 ml-5 mr-5 px-8 py-3  bg-primary-200 hover:bg-primary-500 w-52 h-21 rounded-3xl cursor-pointer">
                        <div class="flex items-center">
                        <ClockOutlineIcon :size="17" />
                        <div class="text-sm pl-4 font-bold text-primary-600">通知</div>
                        </div>
                    </div>
                    </div>
                </div>
        </div>
    `,
})

new Vue({
    el: '#app',
})