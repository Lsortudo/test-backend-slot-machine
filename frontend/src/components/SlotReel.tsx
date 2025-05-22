import { SlotSymbol } from './SlotSymbol';

interface SlotReelProps {
  symbol: string;
  isSpinning: boolean;
}

export const SlotReel = ({ symbol, isSpinning }: SlotReelProps) => {
  return (
    <div className="w-32 h-32 bg-[#1a1a2e] rounded-lg border-2 border-purple-500/30 flex items-center justify-center overflow-hidden">
      <SlotSymbol symbol={symbol} isSpinning={isSpinning} />
    </div>
  );
};