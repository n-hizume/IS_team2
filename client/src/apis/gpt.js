// import { BASE_URL } from "./mail"
// import axios from 'axios'

export const translateByGpt = async (text, level=0) => {
    // const res =  await axios.post(BASE_URL+'/translation/gpt/', {
    //     "word": text,
    //     "level": level
    // })
    // return res.data["translated_words"]
    
    console.log(text, level)
    await new Promise(resolve => setTimeout(resolve, 5000));
    return [
        text +"のダミーアンサーひとつめです", 
        text +"のダミーアンサーふたつめです", 
        text +"のダミーアンサーみっつめです",
        text +"のダミーアンサーよっつめです",
        text +"のダミーアンサーいつつめです",
        text +"のダミーアンサーむっつめです",
    ]
}