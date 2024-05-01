import {render} from '@testing-library/vue'
import Priority from './Priority.vue'

test('render Priority component', () => {
    const { debug } = render(Priority, {
        props: {
            priority: 1,
        }
    })
})