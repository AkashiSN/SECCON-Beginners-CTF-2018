const puppeteer = require("puppeteer");

let origin  = process.env.origin;
let flag = process.env.flag;
let post_id  = process.env.post_id;

(async () => {
    const opt = {
        executablePath: 'google-chrome-stable',
        headless: true,
        args: [
            "--no-sandbox",
            "--disable-background-networking",
            "--disable-default-apps",
            "--disable-extensions",
            "--disable-gpu",
            "--disable-sync",
            "--disable-translate",
            "--hide-scrollbars",
            "--metrics-recording-only",
            "--mute-audio",
            "--no-first-run",
            "--safebrowsing-disable-auto-update",
            `--user-agent=${flag}`
        ],
    };
    const browser = await puppeteer.launch(opt);
    const page = await browser.newPage();
    await page.goto(`${origin}/posts/${post_id}`, {waitUntil: 'domcontentloaded'});
    await page.type('input[name="comment_content"]', '投稿ありがとうございます。大変参考になりました。');
    await page.click('button[type=submit]');
    await page.waitFor(1000);
    await browser.close();
})();
