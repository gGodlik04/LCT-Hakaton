<template>
    <div class="modal" @click="hideModal" v-if="show === true ">
        <div @click.stop class="modal__content-dialog">
            <slot></slot>
        </div>
    </div>
</template>

<script setup>
import {defineEmits} from 'vue'

name: 'ModalWindow';

const props = defineProps({
    show: {
        type: Boolean,
        default: false,
    }
})

const emit = defineEmits(['visibleModal'])

const hideModal = () => {
    emit('visibleModal')
    console.log('da');
}
</script>

<style scoped lang="scss">
.modal {
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background-color: var(--color-accent);
    position: fixed;
    display: flex;
}

.modal__content-dialog {
    color: var(--font-color);
    margin: auto;
    background-color: var(--color-primary);
    padding: 1.5rem;
    min-height: 15rem;
    min-width: 30em;

    border-radius: 20px;
    border: 3px solid var(--color-border-modal);
    box-shadow: 0px 0px 17px 0px rgba(125, 125, 125, 0.25);
}
</style>