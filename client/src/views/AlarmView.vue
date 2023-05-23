<template>
  <div class="bg-white h-screen">
   
    <div class="flex">  
      <SideMenu/>

      <div class="mail-box m-3 rounded-2xl flex">
            
        <AllMail :serverData="serverData" :selectedMail="selectedMail" :mails="mails" @update:selectedMail="updateSelectedMail">
          通知</AllMail>    
        
        <!-- <MailDetail :mail="selectedMail" /> -->

        <router-view></router-view>

      </div>
                
    </div>
  </div>  
  

</template>

<script setup>

import { ref } from 'vue';
import SideMenu from '@/components/SideMenu.vue';
//import SettingInformation from '@/components/SettingInformation.vue';
import AllMail from '@/components/AllMail.vue';
//import NormalView from '@/components/NormalView.vue';
//import WriteView from '@/components/WriteView.vue';
//import MailDetail from '@/components/MailDetail.vue';
//import Share from "vue-material-design-icons/ShareOutline.vue";
//import ReplyAll from "vue-material-design-icons/ReplyAllOutline.vue";
//import Reply from "vue-material-design-icons/ReplyOutline.vue";
//import Information from "vue-material-design-icons/InformationOutline.vue";
import Allmail from './Allmail.vue';



const selectedMail = ref(null);

const updateSelectedMail = (mail) => {
  selectedMail.value = mail;
};





</script>

,

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