<!-- This is where the questions will be typed -->
<script>
export default {
    data() { return { text: '' } },
    mounted() {
        this._onSlash = (e) => {
            // ignore if modifier keys are pressed
            if (e.ctrlKey || e.metaKey || e.altKey) return
            // only respond to the plain slash key
            if (e.key !== '/') return
            //ignore if user is already typing in a field
            const tg = e.target
            if(tg && (tg.tagName == 'INPUT' || tg.tagName === 'TEXTAREA' || tg.isContentEditable)) return

            e.preventDefault()
            const el = this.$refs.inputRef
            if (el && typeof el.focus === 'function') {
                el.focus()
                //put cursor at end
                const len = el.value?.length || 0
                if (el.setSelectionRange) el.setSelectionRange(len, len)
            }
        }
        window.addEventListener('keydown', this._onSlash)
    },
    beforeUnmount() {
        window.removeEventListener('keydown', this._onSlash)
    },
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
            ref="inputRef"
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
        top: 10px;
    }
}
</style>