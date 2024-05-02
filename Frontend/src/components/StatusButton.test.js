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

test('throwing an error when rendering a Priority ', () => {
    consoleErrorSpy = jest.spyOn(console, 'warn').mockImplementation(() => {});

    const errorText = `Invalid prop: type check failed for prop "status"`;
    const options = {
        props: {
            status: 'error'
        }
    }

    render(StatusButton, options);

    expect(consoleErrorSpy).toHaveBeenCalled();
    expect(consoleErrorSpy.mock.calls.some(call => call[0].includes(errorText))).toBe(true);
})