<template>
  <div class="writebox ml-4 mr-6">
    <div class="right w-full mt-4" :style= "{ height: showReplyForm ? '355px' : 'auto' }"> 
      <div class="right-top flex justify-between" :style= "{ height: showReplyForm ? '30px' : '69px' }">
        <div class="flex">
          <!-- <router-link to="/email">
                <IconComponent
                  iconString="back"
                  :iconSize="19"
                  hoverColor="hover:bg-gray-100"
                />
            </router-link> -->
          <!--Menu :size="27" /-->
          <div class="flex" v-if="!showReplyForm">
            <div class="reply justify-center my-2 ml-4 px-3 py-3  bg-primary-700 hover:bg-primary-800 rounded-3xl cursor-pointer" 
            @click="toggleReply">
              <div class="flex items-center text-primary-600">
                <Reply :size="27" />
                <div class="text-xl font-bold ml-2" >
                  返信
                </div>
              </div>  
            </div>
            
            <div class="replyforall my-4 ml-2 px-3 py-3  bg-primary-700 hover:bg-primary-800 rounded-3xl cursor-pointer"
            @click="movewriteScreen">
              <div class="flex text-center text-primary-600">
                <ReplyAll :size="20" />
                <div class="text-sm font-bold ml-2 ">
                  全員に返信
                </div>
              </div>  
            </div>
            <div class="transfer my-4 ml-2 px-3 py-3  bg-primary-700 hover:bg-primary-800 rounded-3xl cursor-pointer"
            @click="movewriteScreen">
              <div class="flex text-center text-primary-600">
                <Share :size="20" />
                <div class="text-sm font-bold ml-2">
                  転送
                </div>
              </div>  
            </div>
          </div>  
        </div>  
        <div class="mt-1 ml-2 mr-3 mb-2.5 cursor-pointer">
          <SettingInformation :threadId="mail.threadId"/>
        </div>  

      </div>
      <div class="mailcontents w-full flex">
        <!-- <img
          class="rounded-full mt-8 mx-5 custom-img"
          src="https://via.placeholder.com/45"
        /> -->
        <div class="w-full my-4 mx-5">
          <div class="font-semibold text-sm mt-4 mb-4">
            <div class="w-full flex justify-between items-center text-zinc-800">
              <!-- <div>{{ email.fromEmail }}</div> -->
              <!-- hirayamasaki@kuhp-kyoto-u.ac.jp -->
              {{ mail.from }}
              <!-- <div class="mr-5 text-xs font-normal">{{ email.createdAt }}</div> -->
              <div class="mr-2 text-xs font-normal text-zinc-700">{{ mail.date }}</div>
            </div>
            <span class="text-xs text-gray-500 font-normal">to me</span>
          </div>
          <!-- <div>{{ email.body }}</div> -->
          
          <div class="mailbody py-2 text-zinc-700" style="overflow: scroll;" :style ="{ height: showReplyForm ? '220px' : '595px' }">
            <p v-html="mail.body"></p>
          </div>
           
        </div>
      </div>
      
    </div>  
    <div v-if="showReplyForm">
      <div v-if="isTranslating">
        <el-progress
          :percentage="100"
          status="success"
          :indeterminate="true"
          :duration="5"
        />
      </div>
      <div class="write mt-1.5">
        <div class="write2-top flex items-center justify-between w-full text-sm px-3.5 py-2.5 bg-primary-700 ">
          <div class="flex text-zinc-700">
            <Reply :size="20" />
            <div class="ml-1.5">{{ mail.from }}</div>
          </div>
          <div class="cursor-pointer text-primary-600">
            <Close :size="20" @click="closeReplyForm"/>
          </div>  
        </div>

        <input type="text" v-model="replySubject" style="resize:none;" class="replysubject w-full
              border-transparent 
              border-none 
              focus:ring-0 
              outline-none
              bg-primary-700
              text-zinc-700
              " rows="2" placeholder="Subject">
        

        <textarea @keydown="onKeyDown" v-model="replyBody" style="resize:none;" class=" textarea w-full 
              border-transparent 
              border-none 
              focus:ring-0 
              outline-none
              bg-primary-700
              -mt-1.5
              text-zinc-700
              
              " rows="14" placeholder="Message">
                
        </textarea>
        <div class="smartgpt flex text-xs font-medium text-primary-600 mr-2">
          <button v-for="result in results" :key="result.id" class="result-item rounded-3xl m-1 hover:bg-primary-1000" :style="getButtonStyle(result)"
          @click="updateTextarea(result)">
            <div class="mx-2 my-0.5" v-if="showButtons">
              {{ result }}
            </div>
          </button>
        </div>
        <div class="write2-b flex justify-between bg-primary-700 -mt-1.5">
          <button @click="sendEmail" class="send 
            bg-primary-300 
            hover:bg-primary-900 
            text-white 
            text-lg 
            font-bold 
            rounded-full
            px-3
            mt-1
            ml-3
            justify-center
            ">
              <SendOutlineIcon :size="17" />
              <div class="ml-2">
                送信
              </div>  
          </button>
          <duv class="tranlatebutton flex font-medium text-primary-600 mt-2 mr-3">
            <!-- bg-primary-300 text-white -->
            <button @click="changeLevel(0)" :class="{'active': translateLevel===0}" class="low bg-primary-700">low</button>
            <button @click="changeLevel(1)" :class="{'active': translateLevel===1}" class="middle bg-primary-700">middle</button>
            <button @click="changeLevel(2)" :class="{'active': translateLevel===2}" class="high bg-primary-700">high</button>
          </duv>

        </div>  
        </div> 
    </div>
  </div>  
         
        
</template>

<script setup>
import Share from "vue-material-design-icons/ShareOutline.vue";
import ReplyAll from "vue-material-design-icons/ReplyAllOutline.vue";
import Reply from "vue-material-design-icons/ReplyOutline.vue";
import SettingInformation from '@/components/SettingInformation.vue';
// import IconComponent from "@/components/IconComponent.vue";
import Close from "vue-material-design-icons/Close.vue";
import SendOutlineIcon from "vue-material-design-icons/SendOutline.vue";
import { useRouter } from "vue-router";
import store from '@/store/index';
import { watch, ref } from 'vue';
import { translateByGpt } from "@/apis/gpt";
import { sendMail } from "@/apis/mail";


var router = useRouter();
var mailId = router.currentRoute.value.query.id;
var mail = store.getters.getMailById(mailId);
var isTranslating = ref(false)

const replyBody = ref("");
const replySubject = ref("Re: " + mail.subject);
const translateLevel = ref(0);


// メールidが変更されたらそのメールの内容に変更
watch(
  () => router.currentRoute.value.query.id,
  (newMailId) => {
    mailId = newMailId;
    mail = store.getters.getMailById(mailId);
    replyBody.value = "";
    replySubject.value = "Re: " + mail.subject;
  }
);

const results = ref([]);

const setTransform = async (newReplyBody) => {
  const lastChar = newReplyBody.slice(-1);
  if (lastChar === "、" || lastChar === "。") {
    const messages = newReplyBody.split(/。|、/);
    const lastMessage = messages[messages.length - 2];
    isTranslating = true
    const translationResults = await translateByGpt(lastMessage.replaceAll("\n", ""), translateLevel);
    console.log(translationResults)
    const punctuatedResults = translationResults
                                .map(res => res.replaceAll("。", "").replaceAll("、", ""))
                                .map(result => result + lastChar + " ");
    const top3Results = punctuatedResults.slice(0, 3);
    results.value = top3Results;
    isTranslating = false
  } else {
    results.value = [];
    showButtons = false;
  }
}

// メッセージが変更されて、最後の１文字が「、」「。」ならgpt変換
watch(
  replyBody,
  setTransform
);

const onKeyDown = (event) => {
  if (event.key !== "Enter") {
    results.value = [];
    showButtons = false;
  }
}


const getButtonStyle = (result) => {
  const textLength = result.length;
  const minHeight = "10px"; // 最低限の高さ（ピクセル単位）を設定する
  const buttonHeight = `${Math.max(textLength * "2px", minHeight)}`;
  const buttonWidth = "400px"; // 幅をテキストの長さに応じて調整する例
  return {
    height: buttonHeight,
    width: buttonWidth,
  };
};


let showButtons = true;

const updateTextarea = (result) => {
  // replyBody.value = result
  const replyWithoutLastChar = replyBody.value.slice(0, -1);
  const messages1 = replyWithoutLastChar.split(/。|、/);
  const messages2 = replyWithoutLastChar.split("。");
  const messages3 = replyWithoutLastChar.split("、");

  // 最後のメッセージの一個前が、「。」だった場合
  if(messages1[messages1.length-1] === messages2[messages2.length-1]){
    messages2[messages2.length-1] = result;
    replyBody.value = messages2.join('。');
  }

  // 最後のメッセージの一個前が、「、」だった場合
  if(messages1[messages1.length-1] === messages3[messages3.length-1]){
    messages3[messages3.length-1] = result;
    replyBody.value = messages3.join('、');
  }

  showButtons = false;
  results.value = []; // ボタン表示をクリアする
};

// 以下の watch 関数を追加
watch(
  () => replyBody.value,
  () => {
    showButtons = true;
    results.value = []; // ボタン表示をクリアする
  }
);


window.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    showButtons = true;
  }
});

const showReplyForm = ref(false);
const toggleReply = () => {
  showReplyForm.value = !showReplyForm.value;
  replySubject.value = "Re: " + mail.subject;
};

const closeReplyForm = () => {
  showReplyForm.value = false;
};

const sendEmail = async () => {
  const res = await sendMail(mail.from, replySubject.value, replyBody.value); 
  console.log(res);
  replyBody.value = "";
  closeReplyForm();
}

const changeLevel = (level) => {
  translateLevel.value = level;
  setTransform(replyBody.value);
}



</script>

<style scoped lang="scss">


  .right {
    width: 100%;
    height: 100%;
    background: #FDFDFD;
    border-radius: 15px 15px 15px 15px;
    box-shadow: 0 0px 20px 0 rgba(0, 0, 0, .03);
    
  }


  .right-top{
    width:100%;
    height:69px;
    background: #D6E9D8;
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
  .reply:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.17);
}
  .replyforall{
    width:125px;
    height:40px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
  }
  .replyforall:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.17);
  }
  .transfer{
    width:90px;
    height:40px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
  }
  .transfer:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.17);
  }
  
  .writebox{
    display: flex;
    flex-direction: column;
    width: 95%;
    height: 90%;
    
    
  }

  .write {
    width: 100%;
    height: 440px;
    position: relative;
  }

  .write2-top {
    border-radius: 15px 15px 0 0;
    height: 30px;
    background: #D6E9D8;
  }

  .replysubject{
    height: 28px;
  }
  
  .write2-b {
    height: 50px;
    border-radius:0 0 15px 15px;
  }

  .textarea {
    height:301px
  }

  .mailcontents {
    height: 695px;
  }

  .low {
    display: grid;
    place-items: center;
    width:70px;
    height:30px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .09);
    border-radius: 15px 0px 0px 15px;
  }

  .middle {
    display: grid;
    place-items: center;
    width:70px;
    height:30px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .09);
    border-radius: 0px 0px 0px 0px;
  }

  .high {
    display: grid;
    place-items: center;
    width:70px;
    height:30px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .09);
    border-radius: 0px 15px 15px 0px;
  }

  .low:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.2);
  }
  .middle:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.2);
  }
  .high:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.2);
  }

  .send{
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.17);
}
  .send:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.2);
  }

  .active {
    background: #467B55;
    color: white;
  }

  .smartgpt {
  position: absolute;
  width: 100%;
  bottom: 100px;
}

.result-item {
  width:400px;
  background: #FDFDFD;
  border: 1px solid;
  border-color: #467B55
}
.result-item:hover {


}



#NewMessageSection {
  overflow: hidden;
  width: 560px;
  height: 570px;
}
</style>