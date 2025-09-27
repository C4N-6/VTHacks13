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
    top: 50%;
    display: flex;
    max-width: 720px;
    align-items: center;
    margin: 10px 50px 10px 10px;
}
.question {
    flex: 1;
    width: 500px;
    height: 50px;
    padding: 10px; /* reserve space for button */
    border-radius: 10px;
    box-sizing: border-box;
}
.send-btn {
    height: 50px;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
    cursor: pointer;
}

@media (max-width: 400px) {
    .question {
        top: 10%;
    }
}
</style>