//This function just prints out some environment variables to make sure they're set up properly
export const test_env = () => {
    console.log('trying to set up enviroment variables...')
    console.log("VITE_TEST_ENV_VAR: " + import.meta.env.VITE_TEST_ENV_VAR)
    console.log("env is dev: " + import.meta.env.DEV)
    console.log('environment variables setup done')
}