<!-- This is where the answer will be -->
<script>
export default {
    name: 'Answer',
    props: {
        title: {
            type: String,
            default: ''
        }
    }
}
</script>

<template>
    <div class="answer">
        <h1 v-if="title">{{ title }}</h1>
        <!-- other answer contents -->
    </div>
</template>

<style>

</style>