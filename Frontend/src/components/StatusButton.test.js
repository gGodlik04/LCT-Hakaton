import {render} from '@testing-library/vue';
import StatusButton from './StatusButton.vue';


test('render statusButton', () => {
    const options = {
        props: {
            status: 3
        }
    }

    const {} = render(StatusButton, options);
})