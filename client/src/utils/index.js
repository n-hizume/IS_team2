import store from '@/store/index';
import { getMails } from '@/apis/mail.js';


export function formatDate(date_str) {
  if(!date_str) return "";

  const date = new Date(date_str);
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

export async function storeMails() {
  const mails = await getMails();
  const mailDatas = [];
  for(const mail of mails){  
    mailDatas.push({
      "id": mail.id, //メールのID
      "threadId": mail.threadId, //メールのスレッドID
      "snipet": mail.snipet, //メールのスニペット(本文の書式なしデータのようなもの)
      "body": mail.body, //本文(書式や改行なども含む)
      "subject": mail.subject, //メールのタイトル
      "from": mail.from, //送信者
      "to": mail.to, //受信者(=自分)
      "date": formatDate(mail.date),
      "expiry": formatDate(mail.expiry),
    });
  }
  store.commit('setMails', mailDatas);
}


export function getAllMails(isAlarm=false) {
  const mailDatas = store.state.mails;
  if(!isAlarm) return mailDatas;

  const sortedmails = mailDatas.filter(mail => mail.expiry).sort((a, b) => {
    if (a.expiry === "今日" && b.expiry !== "今日") {
      return -1; 
    } else if (a.expiry !== "今日" && b.expiry === "今日") {
      return 1; 
    } else {
      return 0; 
    }
  });

  return sortedmails;
  
}

export function getAllMailsForAlarm() {
  return getAllMails(true);
}
