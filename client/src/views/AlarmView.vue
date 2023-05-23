<template>
  <div class="bg-white h-screen">
   
    <div class="flex">  
      <SideMenu/>

      <div class="mail-box m-3 rounded-2xl flex">
            
         
        <AllAlarm/>
        <!-- <MailDetail :mail="selectedMail" /> -->

        
        <router-view></router-view>

      </div>
                
    </div>
  </div>  
  

</template>

<script setup>


import SideMenu from '@/components/SideMenu.vue';
//import AllMail from '@/components/AllMail.vue';
import AllAlarm from '@/components/AllAlarm.vue';
//import { useRouter } from "vue-router";
import store from '@/store/index';






function formatDate(date) {
  const today = new Date(); // 今日の日付を取得
  const yesterday = new Date(today); // 今日の日付をコピーして昨日の日付を作成
  yesterday.setDate(yesterday.getDate() - 1); // 昨日の日付に変更

  const month = date.getMonth() + 1;
  const day = date.getDate();

  if (
    date.getDate() === today.getDate() &&
    date.getMonth() === today.getMonth() &&
    date.getFullYear() === today.getFullYear()
  ) {
    return "今日";
  } else if (
    date.getDate() === yesterday.getDate() &&
    date.getMonth() === yesterday.getMonth() &&
    date.getFullYear() === yesterday.getFullYear()
  ) {
    return "昨日";
  } else {
    return month + "月" + day + "日";
  }
}

const mailDatas = [];

for(const mail of store.state.mails){
  


  
  if (!mail.expiry){
    continue;
  }
  var date = new Date(mail.date);
  var expiry = new Date(mail.expiry);
  

mailDatas.push({
  "id": mail.id, //メールのID
  "threadId": mail.threadId, //メールのスレッドID
  "snipet": mail.snipet, //メールのスニペット(本文の書式なしデータのようなもの)
  "body": mail.body, //本文(書式や改行なども含む)
  "subject": "test: from isteam2 to hizumee228", //メールのタイトル
  "from": "Naoki Hizume <ku.is.team2@gmail.com>", //送信者
  "to": "hizumee228@gmail.com", //受信者(=自分)
  "date": formatDate(date),
  "expiry": formatDate(expiry),
});
  
}



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




  .mail-box {
    width: 90%;
    height: 799px;
    background: #F4F4F3;
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

  .mailbox{
    height: 739px;
    background: #F4F4F3;
  }

  

  .date.expirynotempty {
    display: none
  }






#NewMessageSection {
  overflow: hidden;
  width: 560px;
  height: 570px;
}
</style>