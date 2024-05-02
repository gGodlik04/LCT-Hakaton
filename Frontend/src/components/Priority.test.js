import {render, screen} from '@testing-library/vue'
import Priority from './Priority.vue'

test('render Priority component', () => {
    const options = {
        props: {
            priority: 1
        }
    }

    const { container } = render(Priority, options);

    const element = container.getElementsByClassName('priority-icon');

    expect(element.length).toBeGreaterThan(0);
})