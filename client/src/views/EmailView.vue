<template>
  <div class="bg-white h-screen">
   
    <div class="flex">  
      <SideMenu/>

      <div class="mail-box m-3 rounded-2xl flex">
            
        <AllMail :isAlarm="false"/>
        
        <!-- <MailDetail :mail="selectedMail" /> -->

        <router-view></router-view>
        <!-- <WriteView/> -->

      </div>
                
    </div>
  </div>  
  

</template>

<script setup>

import SideMenu from '@/components/SideMenu.vue';
import AllMail from '@/components/AllMail.vue';

// var serverData = { 
//     "mails":[
//         {   
//             "id":"abcdefg", //メールのID
//             "threadId": "hijklmn", //メールのスレッドID
//             "snipet": "これはテストです。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。これはテストです。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。これはテストです。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。これはテストです。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。これはテストです。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。", //メールのスニペット(本文の書式なしデータのようなもの)
//             "body": "これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\nこれはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\nこれはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n", //本文(書式や改行なども含む)
//             "subject": "test: from isteam2 to hizumee228", //メールのタイトル
//             "from": "Saki Hirayama <saki@kyoto-u.ac.jp>", //送信者
//             "to": "hizumee228@gmail.com", //受信者(=自分)
//             "date": "2023-05-17T00:00+09:00", //メールの受信日時
//             "expiry": "2023-05-17T00:00+09:00" //我々のアプリで設定されたメールの締め切り日時(設定していなければnull)
//         },
//         {   
//             "id":"opqrstu",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": ""
//         },
//         {   
//             "id":"aaaaaaa",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": ""
//         },
//         {   
//             "id":"aaaaaaa",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": ""
//         },
//         {   
//             "id":"aaaaaaa",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": "2023-05-27T00:00+09:00"
//         },
//         {   
//             "id":"aaaaaaa",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": ""
//         },
//         {   
//             "id":"aaaaaaa",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": ""
//         },
//         {   
//             "id":"aaaaaaa",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": "2023-05-23T00:00+09:00"
//         },
//         {   
//             "id":"aaaaaaa",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": "2023-05-25T00:00+09:00"
//         },
//         {   
//             "id":"aaaaaaa",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": "2023-05-25T00:00+09:00"
//         },
//         {   
//             "id":"aiuhgrk",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-10T00:00+09:00",
//             "expiry": "2023-05-24T00:00+09:00"
//         },
//         {   
//             "id":"adjhgek",
//             "threadId": "vwxyz",
//             "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
//             "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
//             "subject": "test ver 2",
//             "from": "Naoki Hizume <ku.is.team2@gmail.com>",
//             "to": "hizumee228@gmail.com",
//             "date": "2023-05-16T00:00+09:00",
//             "expiry": ""
//         },
        
//     ]

// }

// console.log(store.auth)
// store.commit('setMails', serverData.mails);



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