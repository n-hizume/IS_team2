<template>
  <div class="right ml-3 mr-6 mt-5 mb-4 w-full">    
    <div class="right-top flex">
      <router-link to="/email">
            <IconComponent
              iconString="back"
              :iconSize="19"
              
              
              hoverColor="hover:bg-gray-100"
            />
          </router-link>
      <!--Menu :size="27" /-->
      <div class="reply justify-center my-2 ml-4 px-3 py-3  bg-primary-700 hover:bg-primary-500 rounded-3xl cursor-pointer" @click="movewriteScreen">
        <div class="flex items-center">
          <Reply :size="27" />
          <div class="text-xl font-bold ml-2 text-primary-600" >
            返信
          </div>
        </div>  
      </div>
      <div class="replyforall my-4 ml-2 px-3 py-3  bg-primary-700 hover:bg-primary-500 rounded-3xl cursor-pointer"
      @click="movewriteScreen">
        <div class="flex text-center">
          <ReplyAll :size="20" />
          <div class="text-sm font-bold ml-2 text-primary-600">
            全員に返信
          </div>
        </div>  
      </div>
      <div class="transfer my-4 ml-2 px-3 py-3  bg-primary-700 hover:bg-primary-500 rounded-3xl cursor-pointer"
      @click="movewriteScreen">
        <div class="flex text-center">
          <Share :size="20" />
          <div class="text-sm font-bold ml-2 text-primary-600">
            転送
          </div>
        </div>  
      </div>
      <div class="ml-auto mb-11 mt-0.5 mr-3 cursor-pointer">
        <SettingInformation/>
      </div>  

    </div>
    <div class="w-full flex">
      <!-- <img
        class="rounded-full mt-8 mx-5 custom-img"
        src="https://via.placeholder.com/45"
      /> -->
      <div class="w-full my-4 mx-0.5">
        <div class="font-semibold text-sm mt-4 mb-4">
          <div class="w-full flex justify-between items-center">
            <!-- <div>{{ email.fromEmail }}</div> -->
            <!-- hirayamasaki@kuhp-kyoto-u.ac.jp -->
            {{ mail.from }}
            <!-- <div class="mr-5 text-xs font-normal">{{ email.createdAt }}</div> -->
            <div class="mr-5 text-xs font-normal">{{ mail.date }}</div>
          </div>
          <span class="text-xs text-gray-500 font-normal">to me</span>
        </div>
        <!-- <div>{{ email.body }}</div> -->
        <div>{{ mail.body }}</div>
      </div>
    </div>
  </div>  
    
         
        
</template>

<script setup>
import Share from "vue-material-design-icons/ShareOutline.vue";
import ReplyAll from "vue-material-design-icons/ReplyAllOutline.vue";
import Reply from "vue-material-design-icons/ReplyOutline.vue";
import SettingInformation from '@/components/SettingInformation.vue';
import IconComponent from "@/components/IconComponent.vue";
import { useRouter } from "vue-router";
import store from '@/store/index';

const router = useRouter()
const movewriteScreen = () => {
  router.push('/write')
};

// import { defineProps } from 'vue';

// defineProps({
//   mail: {
//     type: Object,
//     required: true
//   }
// });

// const mail = $router.params.mail;
const mail = store.state.focus_mail;

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
    width: 95%;
    height: 763px;
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
    width:255px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
  }
  .allmail{
    width:450px
  }




#NewMessageSection {
  overflow: hidden;
  width: 560px;
  height: 570px;
}
</style>