<template>
    <div class="side-menu-bar flex">
      <div class="flex  w-full">
        <div class="side-menu">
          <div @click="newMessageOpen = true" class="
              flex
              items-center
              justify-center
              bg-primary-100 w-52 
              text-primary-600
              
              h-20
              mt-10
              rounded-2xl
              ml-5
              p-7
              cursor-pointer
            ">
            <PencilOutlineIcon :size="27" class="mr-2" />
            <span class="text-sm font-bold">メール作成</span>
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


              <div class="flex items-center text-primary-600"> 
                <div class="mr-1">
                  <InboxIcon :size="17" />
                </div>  
                <div class="text-sm pl-4 font-bold text-align-left">受信箱</div>
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
            <div class="flex items-center text-primary-600">
             <FileOutlineIcon :size="17" />
              <div class="text-sm pl-5 font-bold">下書き</div>
            </div>
          </div>

          <div class=" flex justify-center mt-2 ml-5 px-8 py-3  bg-primary-200 hover:bg-primary-500 w-52 h-21 mr-5 rounded-3xl cursor-pointer">
            <div class="flex items-center text-primary-600">
              <div class="ml-2">
                <SendOutlineIcon :size="17" />
              </div>  
              <div class="text-sm pl-3 font-bold">送信済み</div>
            </div>
          </div>

          <div
            class=" flex justify-center mt-2 ml-5 mr-5 px-8 py-3  bg-primary-200 hover:bg-primary-500 w-52 h-21 rounded-3xl cursor-pointer">
            <div class="flex items-center text-primary-600">
              <div class="mr-1">
                <TrashCanOutline :size="17" />
              </div>  
              <div class="text-sm pl-4 font-bold">ゴミ箱</div>
            </div>
          </div>

          <div @click="movealarmScreen" 
            class=" flex justify-center mt-2 ml-5 mr-5 px-8 py-3  bg-primary-200 hover:bg-primary-500 w-52 h-21 rounded-3xl cursor-pointer">
            <div class="flex items-center text-primary-600">
              <div class="mr-3">
                <ClockOutlineIcon :size="17" />
              </div>  
              <div class="text-sm pl-4 mr-1 font-bold">通知</div>
            </div>
          </div>
          <div class="mt-96 ml-5 text-zinc-600">
            <Cog :size="30" />
          </div>
        </div>
      </div>   
    </div>

    <div
      v-if="newMessageOpen"
      v-loading="isPushTransformButton"
      id="NewMessageSection" 
      class="
        absolute 
        bottom-11 
        right-0 
        mr-20 
        rounded-2xl
        shadow-2xl 
        bg-white
      "
    >
      <div class="flex items-center justify-between rounded-t-lg w-full text-sm px-3.5 py-2.5 bg-gray-200">
        <div>New message</div>
        <CloseIcon class="cursor-pointer" @click="newMessageOpen = false" :size="19" />
      </div>

      <div>
        <div class="relative flex items-center px-3.5 py-2">
          <div class="text-sm text-gray-700">To</div>
          <input v-model="toEmail" class="w-full h-6 border-transparent border-none focus:ring-0 outline-none" type="text">
          <div class="absolute border-b w-[calc(100%-30px)] bottom-0"></div>
        </div>
        <div class="relative flex items-center px-3.5 py-2">
          <div class="text-sm text-gray-700">Subject</div>
          <input v-model="subject" class="w-full h-6 border-transparent border-none focus:ring-0 outline-none" type="text">
          <div class="absolute border-b w-[calc(100%-30px)] bottom-0"></div>
        </div>
      </div>

      <div class="m-1">
        <textarea v-model="body"  placeholder="please input content" style="resize:none" class="
            w-full 
            border-transparent 
            border-none 
            focus:ring-0 
            outline-none
          " rows="14"></textarea>
      </div>

    <div class="p-4 mt-5 flex">
        <button @click="sendEmail" class="send 
            bg-primary-300 
            hover:bg-primary-400 
            text-white 
            text-lg 
            font-bold 
            rounded-full
            
            
            justify-center
            
            "
        >
          <div class="mr-2">
              <SendOutlineIcon :size="17" />
          </div>
          送信
        </button>

        <div class="button-space"></div> <!-- 隙間 -->

        <!-- 敬語変換 -->
        <button 
        @click="transformKeigo" 
        class="
          bg-green-700 
          hover:bg-green-600 
          text-white 
          <!-- text-sm  -->
          font-bold 
          py-2 
          px-4 
          text-lg 
          rounded-full
          justify-center
        "
        >
          <div v-if="isPushTransformButton">
            <el-icon :size="17"><Loading /></el-icon>
          </div>
          <div v-else>
            <el-icon :size="17"><EditPen /></el-icon>
            敬語変換
          </div> 
        </button>

    </div>

  </div>
</template>    

<script setup>
import { ref } from "vue";

import TrashCanOutline from "vue-material-design-icons/TrashCanOutline.vue";
import PencilOutlineIcon from "vue-material-design-icons/PencilOutline.vue";
import InboxIcon from "vue-material-design-icons/Inbox.vue";
import ClockOutlineIcon from "vue-material-design-icons/ClockOutline.vue";
import SendOutlineIcon from "vue-material-design-icons/SendOutline.vue";
import FileOutlineIcon from "vue-material-design-icons/FileOutline.vue";
import CloseIcon from "vue-material-design-icons/Close.vue";
import Cog from "vue-material-design-icons/CogOutline.vue";
import {EditPen} from "@element-plus/icons-vue"
import {Loading} from "@element-plus/icons-vue"
import { translateByGpt } from "@/apis/gpt";

// import axios from 'axios';

let newMessageOpen = ref(false)
let toEmail = ref('')
let subject = ref('')
let body = ref('')
// const body = ref('')

import { useRouter } from "vue-router";

const router = useRouter()
const movealarmScreen = () => {
  router.push('/alarm')
};

// const movesendScreen = () => {
//   router.push('/send')
// };

var isPushTransformButton = ref(false)
// var loading = ref(true)

/* const sendEmail = () => {
  // 发起POST请求
  axios
    .post('http://127.0.0.1:8000/', body.value)
    .then((response) => {
      // 请求成功回调
      console.log('POST success');
      console.log('response body:', response.data);
    })
    .catch((error) => {
      // 请求失败回调
      console.error('POST error', error);
    });
}; */

// const transformKeigo = () => {
//   axios
//     .post('http://127.0.0.1:8000/translation/gpt/', { "word": body, "level": 0 })
//     .then((response) => {
//       // body = response.data["translated_words"][0];
//       body.value = response.data.translated_words.join('\n');
//       // const reslist = response.data["translated_words"]
//       // const num = reslist.length()
//     })
//     .catch((error) => {
//       console.error(error);
//     });
// };

const translateLevel = ref(0);

const transformKeigo = () => {
  isPushTransformButton.value = true
  // const translationResults = translateByGpt(body.value, translateLevel);
  translateByGpt(body.value, translateLevel).then(result => {
    body.value = result[0]
    isPushTransformButton.value = false
  }); 
};

</script>

<style lang="scss">

.logo-section {
min-width: 250px
}

.help-icon-gray {
border: 2px solid rgb(132, 132, 132);
}

.input-width {
max-width: 700px;
}

.custom-gray-color {
background-color: rgb(232, 232, 232);
}

.side-menu {
width: 280px;
}

.side-menu-item {
width: 227px;
}

.mail-box {
width: 90%;
height: 799px;
background: #F4F4F3;
}

.right {
width: 63%;
height: 762px;
background: #FDFDFD;
border-radius: 15px 15px 15px 15px;
box-shadow: 0 0px 20px 0 rgba(0, 0, 0, .03);
}

.flexbox {
display: flex;
flex-direction: column;
text-align: center;
width: 300px;
height: 100px;
}

.mail {
width: 400px;
height: 116px;
background: #FDFDFD;
}

.right-top{
width:100%;
height:69px;
background: #FDFDFD;
border-radius: 15px 15px 0 0;
box-shadow: 0 0px 20px 0 rgba(0, 0, 0, .05);
}
.reply{
display: grid;
place-items: center;
width:120px;
height:50px;
box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
}
.replyforall{
width:125px;
height:40px;
box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
}
.transfer{
width:90px;
height:40px;
box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
}
.side-menu-bar{
width:270px;
box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
}
.send{
display:flex;
place-items: center;
width:90px;
height:35px;
box-shadow: 0px 0px 12px 5px rgba(0, 0, 0, .08);
}

.button-space {
  margin-right: 20px; /* 调整空隙的大小 */
}

// .sidebutton :hover {
//   cursor: pointer;
//   box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
// }



#NewMessageSection {
overflow: hidden;
width: 560px;
height: 570px;
}
</style>
