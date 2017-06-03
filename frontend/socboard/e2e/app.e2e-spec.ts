import { SocboardPage } from './app.po';

describe('socboard App', () => {
  let page: SocboardPage;

  beforeEach(() => {
    page = new SocboardPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
