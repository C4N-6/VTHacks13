<!-- This is where the questions will be typed -->
<script>
export default {
    data() { return { text: '' } },
    methods: {
        send() {
            console.log('send:', this.text);
            this.text = '';
        }
    }
}
</script>

<template>
    <div class="question-box">
        <input 
            class="question" 
            placeholder="Ask a question"
            @keyup.enter="send"/>
        <button @click="send" class="send-btn">send</button>
    </div>
</template>

<style>
.quesion-box {
    display: flex;
    max-width: 720px;
    align-items: center;
}
.question {
    flex: 1;
    width: 100%;
    padding: 10px 110px 10px 12px; /* reserve space for button */
    border-radius: 10px;
    box-sizing: border-box;
}
.send-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
    cursor: pointer;
}
</style>