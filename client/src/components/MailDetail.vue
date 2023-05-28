<template>
  <div class="writebox ml-4 mr-6">
    <div class="right w-full mt-4" :style= "{ height: showReplyForm ? '355px' : 'auto' }"> 
      <div class="right-top flex justify-between" :style= "{ height: showReplyForm ? '36px' : '69px' }">
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
            <div class="reply justify-center my-2 ml-4 px-3 py-3  bg-primary-700 hover:bg-primary-500 rounded-3xl cursor-pointer" 
            @click="toggleReply">
              <div class="flex items-center text-primary-600">
                <Reply :size="27" />
                <div class="text-xl font-bold ml-2" >
                  返信
                </div>
              </div>  
            </div>
            
            <div class="replyforall my-4 ml-2 px-3 py-3  bg-primary-700 hover:bg-primary-500 rounded-3xl cursor-pointer"
            @click="movewriteScreen">
              <div class="flex text-center text-primary-600">
                <ReplyAll :size="20" />
                <div class="text-sm font-bold ml-2 ">
                  全員に返信
                </div>
              </div>  
            </div>
            <div class="transfer my-4 ml-2 px-3 py-3  bg-primary-700 hover:bg-primary-500 rounded-3xl cursor-pointer"
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
        <div class="mt-2 ml-2 mr-3 mb-2 cursor-pointer">
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
      <div class="write mt-1.5">
        <div class="write2-top flex items-center justify-between w-full text-sm px-3.5 py-2.5 bg-primary-700 ">
          <div class="flex text-zinc-700">
            <Reply :size="20" />
            <div class="ml-1.5">{{ mail.from }}</div>
          </div>
          <div class="cursor-pointer text-zinc-600">
            <Close :size="20" @click="closeReplyForm"/>
          </div>  
        </div>

        <textarea v-model="replySubject" style="resize:none; height: 40px" class=" textarea w-full 
              border-transparent 
              border-none 
              focus:ring-0 
              outline-none
              bg-primary-700
              " rows="2" placeholder="Subject">
        </textarea>

        <textarea v-model="replyBody" style="resize:none;" class=" textarea w-full 
              border-transparent 
              border-none 
              focus:ring-0 
              outline-none
              bg-primary-700
              
              " rows="14" placeholder="Message">
                
        </textarea>
        
        <div class="write2-b flex justify-between bg-primary-700 -mt-1.5">
          <button @click="sendEmail" class="send 
            bg-primary-300 
            hover:bg-primary-400 
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
          <duv class="flex font-medium text-primary-600 mt-2 mr-3">
            <button class="low bg-primary-700 hover:bg-primary-500">low</button>
            <button class="middle bg-primary-700 hover:bg-primary-500">middle</button>
            <button class="high bg-primary-700 hover:bg-primary-500">high</button>
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

const replyBody = ref("");
const replySubject = ref("Re: " + mail.subject);

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

// メッセージが変更されて、最後の１文字が「、」「。」ならgpt変換
watch(
  replyBody,
  async (newReplyBody) => {
    const lastChar = newReplyBody.slice(-1);
    if (lastChar === "、" || lastChar === "。") {
      const messages = newReplyBody.split(/。|、/);
      const lastMessage = messages[messages.length - 2];
      const results = await translateByGpt(lastMessage.replaceAll("\n", ""));
      console.log(results)
    }
  }
)


const showReplyForm = ref(false);
const toggleReply = () => {
  showReplyForm.value = !showReplyForm.value;
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
  
  .writebox{
    display: flex;
    flex-direction: column;
    width: 95%;
    height: 90%;
    
    
  }

  .write {
    width: 100%;
    height: 440px;
  }

  .write2-top {
    border-radius: 15px 15px 0 0;
  }
  
  .write2-b {
    height: 50px;
    border-radius:0 0 15px 15px;
  }

  .textarea {
    height:312px
  }

  .mailcontents {
    height: 695px;
  }

  .low {
    display: grid;
    place-items: center;
    width:70px;
    height:30px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
    border-radius: 15px 0px 0px 15px;
  }

  .middle {
    display: grid;
    place-items: center;
    width:70px;
    height:30px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
    border-radius: 0px 0px 0px 0px;
  }

  .high {
    display: grid;
    place-items: center;
    width:70px;
    height:30px;
    box-shadow: 0 0px 15px 0 rgba(0, 0, 0, .08);
    border-radius: 0px 15px 15px 0px;
  }
#NewMessageSection {
  overflow: hidden;
  width: 560px;
  height: 570px;
}
</style>