<script>
import QuestionTextBox from './components/QuestionTextBox.vue';
import Answer from './components/Answer.vue';

export default {
  components: { QuestionTextBox, Answer },
  data() {
    return { headerText: ''}
  },
  methods: {
    handleQuestion(payload) {
      this.headerText = payload
    }
  }
}
</script>

<template>
  <QuestionTextBox @submit="handleQuestion" />
  <Answer :title="headerText" />
</template>
 
<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
