import {render, screen} from '@testing-library/vue'
import ModalLoading from './ModalLoading.vue'

test('render ModalLoading', () => {
    render(ModalLoading)

    expect(screen.getByTestId('modal-loading').innerHTML).toBeTruthy();
})