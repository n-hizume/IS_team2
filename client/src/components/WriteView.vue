<template>
  <div id="WriteView" class="w-full">
    <div class="flex-container">
      <!--メール詳細-->
      <div class="right ml-2 mr-2 mt-5 mb-2 rounded-2xl">

        <!--メール詳細top-->
        <div class="right-top flex">
          

        </div>
      </div>

      <div class="write ml-2 mr-7 ">

        <!--メール詳細top-->
          <div class="write2-top flex items-center ml-2flex justify-between w-full text-sm px-3.5 py-2.5 bg-gray-200">
            <Reply :size="20" />
          </div>

          
          <textarea id="textatra1" name="textarea" v-model="body" style="resize:none;" class="w-full 
                border-transparent 
                border-none 
                focus:ring-0 
                outline-none
                bg-primary-700
                " rows="14">
                  
          </textarea>
          

        <div class="write2-b flex">
          <button @click="sendEmail" class="send 
            bg-primary-300 
            hover:bg-primary-400 
            text-white 
            text-lg 
            font-bold 
            rounded-full
            px-3
            ml-4
            
            
            
            
            
            justify-center
            
              ">
              <SendOutlineIcon :size="17" />
              送信
            </button>
            <Close :size="20"/>

        </div>  
      </div> 
    </div>
  </div>
</template>

<script setup>

import { ref } from "vue";

import Reply from "vue-material-design-icons/ReplyOutline.vue";
import SendOutlineIcon from "vue-material-design-icons/SendOutline.vue";
import Close from "vue-material-design-icons/CloseOutline.vue";


let newMessageOpen = ref(false)
let toEmail = ref('')
let subject = ref('')
let body = ref('')

//import { useRouter } from "vue-router";

//const router = useRouter()

//const moveNextScreen = () => {
  //router.push('/write')
//};


const sendEmail = async () => {
  return 
}


</script>

,

<style lang="scss">

#WriteView {
  overflow: hidden;

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
    width: 95%;
    height: 325px;
    background: #FDFDFD;
    box-shadow: 0 0px 20px 0 rgba(0, 0, 0, .03);
  }

  .write {
    width: 95%;
    height: 427px;
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
    height:30px;
    background: #FDFDFD;
    border-radius: 15px 15px 0 0;
    box-shadow: 0 0px 20px 0 rgba(0, 0, 0, .05);
  }

  .write2-top{
    width:100%;
    height:30px;
    background: #FDFDFD;
    border-radius: 15px 15px 0 0;
    box-shadow: 0 0px 20px 0 rgba(0, 0, 0, .05);
  }

  .write2-b{
    width:100%;
    height:40px;
    background: #FDFDFD;
    border-radius: 0 0 15px 15px;

    
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
    height:36px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
  }
  .transfer{
    width:90px;
    height:40px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
  }
  .side-menu-bar{
    width:255px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
  }
  
  .send{
    display:flex;
    place-items: center;
    width:90px;
    height:35px;
    box-shadow: 0px 0px 12px 5px rgba(0, 0, 0, .08);
  }

  
}

#NewMessageSection {
  overflow: hidden;
  width: 560px;
  height: 570px;
}
</style>