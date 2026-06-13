type Props = {
  title: string;
  time: number;
};

export const RecordCard = (props: Props) => {
  const { title, time } = props;
  return (
    <div>
      <p>タイトル：{title}</p>
      <p>時間：{time}</p>
    </div>
  );
};
